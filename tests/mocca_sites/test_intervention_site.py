from django.test import override_settings, TestCase, tag
from edc_utils import get_utcnow
from mocca_prn.models.integrated_care_clinic_registration import (
    IntegratedCareClinicRegistration,
    IntegratedCareClinicRegistrationError,
)
from mocca_sites.is_intervention_site import is_intervention_site
from tests.mocca_test_case_mixin import MoccaTestCaseMixin


class TestIntervention(MoccaTestCaseMixin, TestCase):
    @tag("interv")
    @override_settings(SITE_ID=103)
    def test_is_intervention(self):
        self.assertTrue(is_intervention_site())

    @tag("interv")
    @override_settings(SITE_ID=101)
    def test_is_not_intervention(self):
        self.assertFalse(is_intervention_site())

    @tag("interv")
    def test_integrated_care_registration(self):
        self.assertRaises(
            IntegratedCareClinicRegistrationError,
            IntegratedCareClinicRegistration.objects.create,
            date_opened=get_utcnow(),
        )
