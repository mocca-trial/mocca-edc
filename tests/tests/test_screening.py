from django.test import TestCase, tag
from django.urls import reverse
from django_webtest import WebTest
from edc_auth import AUDITOR, EVERYONE, SCREENING
from edc_constants.constants import ALIVE, DEAD, FEMALE, MALE, NO, NOT_APPLICABLE, YES
from edc_sites import get_current_country
from model_bakery.baker import make_recipe

from mocca_lists.models import MoccaOriginalSites
from mocca_screening.forms import SubjectScreeningForm
from mocca_screening.models import MoccaRegister, SubjectScreening

from ..mocca_test_case_mixin import MoccaTestCaseMixin


class TestScreening(MoccaTestCaseMixin, WebTest):
    """
    Uganda,Kiswa,KB-0140--1,05-0124,GW,1936,82,Male
    Uganda,Kiswa,KB-0141--1,05-0125,NM,1960,58,Female
    """

    def setUp(self):
        super().setUp()
        self.assertEqual("uganda", get_current_country())
        self.mocca_register = MoccaRegister.objects.get(
            mocca_country=get_current_country(), mocca_study_identifier="05-0125"
        )
        self.mocca_register_male = MoccaRegister.objects.get(
            mocca_country=get_current_country(), mocca_study_identifier="05-0124"
        )
        self.mocca_site = MoccaOriginalSites.objects.get(
            name=self.mocca_register.mocca_site.name
        )

    def test_screening_ok(self):
        for mocca_register in [self.mocca_register, self.mocca_register_male]:
            with self.subTest(mocca_register=mocca_register):
                form = SubjectScreeningForm(
                    data=self.get_subject_screening_form_data(mocca_register=mocca_register),
                    instance=None,
                )
                form.is_valid()
                self.assertEqual(form._errors, {})
                form.save()
                self.assertTrue(SubjectScreening.objects.all()[0].eligible)

    def test_screening_no_matching_site(self):
        data = self.get_subject_screening_form_data(gender=MALE)
        sites = {k: v for k, v in self.mocca_sites.items() if v.name != self.mocca_site.name}
        mocca_site = MoccaOriginalSites.objects.get(name=list(sites)[0])
        data.update(mocca_site=mocca_site)
        form = SubjectScreeningForm(data=data, instance=None)
        form.is_valid()
        self.assertIn("mocca_site", form._errors)

    def test_screening_no_matching_study_identifier(self):
        data = self.get_subject_screening_form_data(gender=MALE)
        data.update(mocca_study_identifier="1111111")
        form = SubjectScreeningForm(data=data, instance=None)
        form.is_valid()
        self.assertIn("mocca_study_identifier", form._errors)

    def test_screening_no_matching_gender(self):
        for mocca_register in [self.mocca_register, self.mocca_register_male]:
            with self.subTest(mocca_register=mocca_register):
                data = self.get_subject_screening_form_data(mocca_register)
                data.update(gender=FEMALE if data.get("gender") == MALE else MALE)
                form = SubjectScreeningForm(data=data, instance=None)
                form.is_valid()
                self.assertIn("gender", form._errors)

    def test_screening_no_matching_initials(self):
        data = self.get_subject_screening_form_data(gender=MALE)
        data.update(initials="XX")
        form = SubjectScreeningForm(data=data, instance=None)
        form.is_valid()
        self.assertIn("initials", form._errors)

    def test_screening_no_matching_birth_year(self):
        data = self.get_subject_screening_form_data(gender=MALE)
        data.update(birth_year=1901)
        form = SubjectScreeningForm(data=data, instance=None)
        form.is_valid()
        self.assertIn("birth_year", form._errors)

    def test_screening_invalid_by_age(self):

        data = self.get_subject_screening_form_data(gender=MALE)

        responses = dict(
            age_in_years=300,
        )

        for k, v in responses.items():
            with self.subTest(k=v):
                data.update({k: v})
                form = SubjectScreeningForm(data=data, instance=None)
                form.is_valid()
                self.assertIn("age_in_years", form._errors)

    def test_screening_care_reason(self):
        data = self.get_subject_screening_form_data(gender=MALE)
        data.update(care=NO)
        form = SubjectScreeningForm(data=data, instance=None)
        form.is_valid()
        self.assertIn("care_not_in_reason", form._errors)

    def test_screening_care_facility_location(self):
        data = self.get_subject_screening_form_data(gender=MALE)
        data.update(
            care=NO, care_not_in_reason="blah blah", care_facility_location="somewhere"
        )
        form = SubjectScreeningForm(data=data, instance=None)
        form.is_valid()
        self.assertIn("care_facility_location", form._errors)

    def test_screening_ineligible(self):

        responses = dict(
            willing_to_consent=NO,
            requires_acute_care=YES,
            care=NO,
            pregnant=YES,
        )
        for gender in [MALE, FEMALE]:
            for k, v in responses.items():
                with self.subTest(k=k, v=v, gender=gender):
                    data = self.get_subject_screening_form_data(gender=gender)
                    data.update({k: v})
                    if k == "pregnant" and gender == MALE:
                        continue
                    if k == "care":
                        data.update(
                            care_not_in_reason="blah blah",
                            care_facility_location=NOT_APPLICABLE,
                            icc=NOT_APPLICABLE,
                            icc_since_mocca=NO,
                        )
                    form = SubjectScreeningForm(data=data, instance=None)
                    form.is_valid()
                    self.assertEqual(form._errors, {})
                    form.save()
                    self.assertFalse(
                        SubjectScreening.objects.get(
                            mocca_study_identifier=data.get("mocca_study_identifier")
                        ).eligible
                    )

    def test_screening_unsuitable(self):

        data = self.get_subject_screening_form_data(gender=FEMALE)
        data.update(unsuitable_for_study=YES)
        form = SubjectScreeningForm(data=data, instance=None)
        form.is_valid()
        form.save()
        self.assertFalse(
            SubjectScreening.objects.get(
                mocca_study_identifier=data.get("mocca_study_identifier")
            ).eligible
        )

    @tag("webtest")
    def test_mocca_register_changelist(self):

        mocca_register_contact = make_recipe(
            "mocca_screening.moccaregistercontact", mocca_register=self.mocca_register
        )

        self.login(superuser=False, groups=[EVERYONE, AUDITOR, SCREENING])
        change_list_url = reverse(
            "mocca_screening_admin:mocca_screening_moccaregister_changelist"
        )
        change_list_url = f"{change_list_url}?q={self.mocca_register.mocca_study_identifier}"
        screening_add_url = reverse(
            "mocca_screening_admin:mocca_screening_subjectscreening_add"
        )
        refusal_add_url = reverse(
            "mocca_screening_admin:mocca_screening_subjectrefusalscreening_add"
        )
        mocca_register_contact.survival_status = ALIVE
        mocca_register_contact.call = NO
        mocca_register_contact.screen_now = NO
        mocca_register_contact.save()
        self.assertTrue(mocca_register_contact.call == NO)
        self.assertTrue(mocca_register_contact.screen_now == NO)
        self.assertTrue(mocca_register_contact.survival_status == ALIVE)
        response = self.app.get(change_list_url, user=self.user, status=200)
        self.assertIn(self.mocca_register.mocca_study_identifier, response)
        self.assertIn(screening_add_url, response)
        self.assertIn(refusal_add_url, response)

        mocca_register_contact.survival_status = DEAD
        mocca_register_contact.save()
        self.assertTrue(mocca_register_contact.survival_status == DEAD)
        response = self.app.get(change_list_url, user=self.user, status=200)
        self.assertNotIn(screening_add_url, response)
        self.assertNotIn(refusal_add_url, response)
