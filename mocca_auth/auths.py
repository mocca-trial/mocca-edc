from edc_action_item.auth_objects import (
    ACTION_ITEM,
    ACTION_ITEM_EXPORT,
    ACTION_ITEM_VIEW_ONLY,
)
from edc_adverse_event.auth_objects import (
    AE,
    AE_REVIEW,
    AE_SUPER,
    TMG,
    TMG_REVIEW,
    TMG_ROLE,
)
from edc_appointment.auth_objects import (
    APPOINTMENT,
    APPOINTMENT_EXPORT,
    APPOINTMENT_VIEW,
)
from edc_auth.auth_objects import (
    AUDITOR,
    AUDITOR_ROLE,
    CLINIC,
    CLINICIAN_ROLE,
    CLINICIAN_SUPER_ROLE,
    NURSE_ROLE,
)
from edc_auth.site_auths import site_auths
from edc_data_manager.auth_objects import (
    DATA_MANAGER_EXPORT,
    DATA_MANAGER_ROLE,
    SITE_DATA_MANAGER_ROLE,
)
from edc_export.auth_objects import DATA_EXPORTER_ROLE
from edc_label.auth_objects import LABELING
from edc_offstudy.auth_objects import OFFSTUDY
from edc_pharmacy.auth_objects import PHARMACIST_ROLE, SITE_PHARMACIST_ROLE
from edc_randomization.auth_objects import RANDO_UNBLINDED, RANDO_VIEW
from edc_screening.auth_objects import SCREENING, SCREENING_VIEW
from edc_unblinding.auth_objects import UNBLINDING_REQUESTORS

from .auth_objects import (
    MOCCA_AUDITOR,
    MOCCA_CLINIC,
    MOCCA_CLINIC_SUPER,
    clinic_codenames,
)

# MOCCA groups
site_auths.add_group(*clinic_codenames, name=MOCCA_AUDITOR, view_only=True)
site_auths.add_group(*clinic_codenames, name=MOCCA_CLINIC, no_delete=True)
site_auths.add_group(*clinic_codenames, name=MOCCA_CLINIC_SUPER)

# update edc roles
site_auths.update_role(
    ACTION_ITEM,
    AE,
    APPOINTMENT,
    MOCCA_CLINIC,
    UNBLINDING_REQUESTORS,
    name=CLINICIAN_ROLE,
)

site_auths.update_role(
    ACTION_ITEM,
    AE_SUPER,
    APPOINTMENT,
    MOCCA_CLINIC_SUPER,
    UNBLINDING_REQUESTORS,
    name=CLINICIAN_SUPER_ROLE,
)

site_auths.update_role(
    ACTION_ITEM,
    AE,
    APPOINTMENT,
    MOCCA_CLINIC,
    name=NURSE_ROLE,
)

site_auths.update_role(
    ACTION_ITEM,
    AE,
    APPOINTMENT,
    CLINIC,
    LABELING,
    MOCCA_CLINIC,
    OFFSTUDY,
    SCREENING,
    TMG,
    name=DATA_MANAGER_ROLE,
)

site_auths.update_role(ACTION_ITEM, UNBLINDING_REQUESTORS, name=TMG_ROLE)

site_auths.update_role(
    ACTION_ITEM_VIEW_ONLY,
    AE_REVIEW,
    APPOINTMENT_VIEW,
    MOCCA_AUDITOR,
    TMG_REVIEW,
    name=AUDITOR_ROLE,
)

site_auths.update_role(
    AUDITOR,
    ACTION_ITEM,
    AE_REVIEW,
    MOCCA_AUDITOR,
    SCREENING_VIEW,
    TMG_REVIEW,
    name=SITE_DATA_MANAGER_ROLE,
)


# data export
site_auths.update_role(
    ACTION_ITEM_EXPORT,
    APPOINTMENT_EXPORT,
    DATA_MANAGER_EXPORT,
    name=DATA_EXPORTER_ROLE,
)

site_auths.update_role(RANDO_UNBLINDED, name=PHARMACIST_ROLE)
site_auths.update_role(RANDO_VIEW, name=SITE_PHARMACIST_ROLE)
