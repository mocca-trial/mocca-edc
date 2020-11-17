from datetime import date

from django.test import TestCase, tag
from edc_constants.constants import (
    YES,
    NO,
    MALE,
    NOT_APPLICABLE,
)
from edc_utils.date import get_utcnow
from mocca_lists.models import MoccaOriginalSites
from mocca_screening.constants import INTEGRATED, NCD_CLINIC
from mocca_screening.forms import SubjectScreeningForm
from mocca_screening.models import MoccaRegister, SubjectScreening

from ..mocca_test_case_mixin import MoccaTestCaseMixin


class TestForms(MoccaTestCaseMixin, TestCase):
    def setUp(self):

        self.mocca_site = MoccaOriginalSites.objects.get(name="hindu_mandal")
        MoccaRegister.objects.create(
            mocca_screening_identifier="XXXXXX",
            mocca_study_identifier="0700001",
            initials="EW",
            gender=MALE,
            dob=date(2000, 6, 15),
            age_in_years=20,
            mocca_country="tanzania",
            mocca_site=self.mocca_site,
        )

    def get_data(self):
        return {
            "screening_consent": YES,
            "report_datetime": get_utcnow(),
            "mocca_participant": YES,
            "mocca_site": str(self.mocca_site.id),
            "mocca_study_identifier": "0700001",
            "initials": "EW",
            "gender": MALE,
            "birth_year": 2000,
            "age_in_years": 20,
            "clinic_type": INTEGRATED,
            "unsuitable_for_study": NO,
            "unsuitable_agreed": NOT_APPLICABLE,
        }

    @tag("123")
    def test_screening_ok(self):

        form = SubjectScreeningForm(data=self.get_data(), instance=None)
        form.is_valid()
        self.assertEqual(form._errors, {})
        form.save()
        self.assertTrue(SubjectScreening.objects.all()[0].eligible)

    def test_screening_invalid(self):

        data = self.get_data()

        responses = dict(age_in_years=17,)

        for k, v in responses.items():
            with self.subTest(k=v):
                data.update({k: v})
                form = SubjectScreeningForm(data=data, instance=None)
                form.is_valid()
                self.assertIn("age_in_years", form._errors)

    def test_screening_ineligible(self):

        data = self.get_data()

        responses = dict(
            qualifying_condition=NO, lives_nearby=NO, requires_acute_care=YES,
        )

        for k, v in responses.items():
            with self.subTest(k=v):
                data.update({k: v})
                form = SubjectScreeningForm(data=data, instance=None)
                form.is_valid()
                self.assertEqual(form._errors, {})
                form.save()

                self.assertFalse(SubjectScreening.objects.all()[0].eligible)

    def test_screening_unsuitable(self):

        data = self.get_data()

        data.update(unsuitable_for_study=YES)
        form = SubjectScreeningForm(data=data, instance=None)
        form.is_valid()
        self.assertIn("reasons_unsuitable", form._errors)

        data.update(reasons_unsuitable="blah blah")
        form = SubjectScreeningForm(data=data, instance=None)
        form.is_valid()
        self.assertIn("unsuitable_agreed", form._errors)

        data.update(unsuitable_agreed=NO)
        form = SubjectScreeningForm(data=data, instance=None)
        form.is_valid()
        self.assertIn("unsuitable_agreed", form._errors)

        data.update(unsuitable_agreed=YES)
        form = SubjectScreeningForm(data=data, instance=None)
        form.is_valid()
        form.save()
        self.assertFalse(SubjectScreening.objects.all()[0].eligible)
