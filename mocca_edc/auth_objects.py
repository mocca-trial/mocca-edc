from django.apps import apps as django_apps

MOCCA_AUDITOR = "MOCCA_AUDITOR"
MOCCA_CLINIC = "MOCCA_CLINIC"
MOCCA_CLINIC_SUPER = "MOCCA_CLINIC_SUPER"
MOCCA_EXPORT = "MOCCA_EXPORT"

clinic_codenames = []
for app_config in django_apps.get_app_configs():
    if app_config.name in [
        "mocca_lists",
    ]:
        for model_cls in app_config.get_models():
            for prefix in ["view"]:
                clinic_codenames.append(
                    f"{app_config.name}.{prefix}_{model_cls._meta.model_name}"
                )

for app_config in django_apps.get_app_configs():
    if app_config.name in [
        "mocca_prn",
        "mocca_subject",
        "mocca_consent",
    ]:
        for model_cls in app_config.get_models():
            for prefix in ["add", "change", "view", "delete"]:
                clinic_codenames.append(
                    f"{app_config.name}.{prefix}_{model_cls._meta.model_name}"
                )
clinic_codenames.sort()


ae_local_reviewer = [
    "mocca_subject.add_aelocalreview",
    "mocca_subject.change_aelocalreview",
    "mocca_subject.delete_aelocalreview",
    "mocca_subject.view_aelocalreview",
    "mocca_subject.view_historicalaelocalreview",
]
ae_sponsor_reviewer = [
    "mocca_subject.add_aesponsorreview",
    "mocca_subject.change_aesponsorreview",
    "mocca_subject.delete_aesponsorreview",
    "mocca_subject.view_aesponsorreview",
    "mocca_subject.view_historicalaesponsorreview",
]
