#     AUDITOR,
# from edc_auth.auth_objects import (
#     CLINIC,
#     get_default_codenames_by_group,
#     CLINIC_SUPER,
# )
# from edc_unblinding.auth_objects import UNBLINDING_REQUESTORS, UNBLINDING_REVIEWERS
# from edc_screening.auth_objects import SCREENING
#
#     auditor,
# from .codenames import (
#     clinic,
#     screening,
#     clinic_super,
#     unblinding_requestors,
#     unblinding_reviewers,
# )
#
#
# def get_codenames_by_group():
#     codenames_by_group = {k: v for k, v in get_default_codenames_by_group().items()}
#     codenames_by_group[AUDITOR] = auditor
#     codenames_by_group[CLINIC] = clinic
#     codenames_by_group[CLINIC_SUPER] = clinic_super
#     codenames_by_group[SCREENING] = screening
#     codenames_by_group[UNBLINDING_REQUESTORS] = unblinding_requestors
#     codenames_by_group[UNBLINDING_REVIEWERS] = unblinding_reviewers
#     return codenames_by_group
#
