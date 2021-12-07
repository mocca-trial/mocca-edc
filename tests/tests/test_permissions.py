from django.test import TestCase
from edc_adverse_event.auth_objects import AE, AE_REVIEW, TMG, ae, tmg
from edc_auth.auth_objects import (
    ACCOUNT_MANAGER,
    AUDITOR,
    CLINIC,
    EVERYONE,
    PII,
    PII_VIEW,
)
from edc_auth.auth_objects.codenames import (  # ae_review,; get_rando,; pii,; pii_view,
    account_manager,
    everyone,
)

# from edc_auth.group_permissions_updater import GroupPermissionsUpdater
from edc_auth.utils import compare_codenames_for_group
from edc_lab.auth_objects import LAB, LAB_VIEW, lab_codenames, lab_view_codenames
from edc_randomization.constants import RANDO
from edc_screening.auth_objects import SCREENING
from edc_unblinding.auth_objects import UNBLINDING_REQUESTORS, UNBLINDING_REVIEWERS

# from mocca_auth.codenames import (
#     auditor,
#     clinic,
#     screening,
#     unblinding_requestors,
#     unblinding_reviewers,
# )
# from mocca_auth.codenames_by_group import get_codenames_by_group


class TestPermissions(TestCase):
    @classmethod
    def setUpClass(cls):
        # GroupPermissionsUpdater(codenames_by_group=get_codenames_by_group(), verbose=True)
        return super(TestPermissions, cls).setUpClass()

    # def test_pii(self):
    #     # update_permissions()
    #     # show_permissions_for_group(group_name=PII)
    #     compare_codenames_for_group(group_name=PII, expected=pii)
    #     # show_permissions_for_group(group_name=PII_VIEW)
    #     compare_codenames_for_group(group_name=PII_VIEW, expected=pii_view)
    #
    def test_ae(self):
        # update_permissions()
        compare_codenames_for_group(group_name=AE, expected=ae)

    def test_ae_review(self):
        # update_permissions()
        compare_codenames_for_group(group_name=AE_REVIEW, expected=ae_review)

    #
    # def test_screening(self):
    #     # update_permissions()
    #     compare_codenames_for_group(group_name=SCREENING, expected=screening)
    #
    # def test_unblinding(self):
    #     # update_permissions()
    #     compare_codenames_for_group(
    #         group_name=UNBLINDING_REVIEWERS, expected=unblinding_reviewers
    #     )
    #     compare_codenames_for_group(
    #         group_name=UNBLINDING_REQUESTORS, expected=unblinding_requestors
    #     )
    #
    def test_everyone(self):
        # update_permissions()
        compare_codenames_for_group(group_name=EVERYONE, expected=everyone)

    # def test_auditors(self):
    #     # update_permissions()
    #     compare_codenames_for_group(group_name=AUDITOR, expected=auditor)

    def test_account_manager(self):
        # update_permissions()
        compare_codenames_for_group(group_name=ACCOUNT_MANAGER, expected=account_manager)

    # def test_clinic(self):
    #     # update_permissions()
    #     compare_codenames_for_group(group_name=CLINIC, expected=clinic)
    #
    # def test_rando(self):
    #     # update_permissions()
    #     compare_codenames_for_group(group_name=RANDO, expected=get_rando())
    #
    def test_lab(self):
        # update_permissions()
        compare_codenames_for_group(group_name=LAB, expected=lab_codenames)
        compare_codenames_for_group(group_name=LAB_VIEW, expected=lab_view_codenames)

    def test_tmg(self):
        # update_permissions()
        compare_codenames_for_group(group_name=TMG, expected=tmg)
