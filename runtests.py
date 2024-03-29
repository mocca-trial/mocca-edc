#!/usr/bin/env python
import logging
import os
import sys
from os.path import abspath, dirname, join

import django
from django.conf import settings
from django.test.runner import DiscoverRunner
from edc_test_utils import DefaultTestSettings
from edc_utils import get_datetime_from_env
from multisite import SiteID

app_name = "mocca_edc"
base_dir = dirname(abspath(__file__))

DEFAULT_SETTINGS = DefaultTestSettings(
    calling_file=__file__,
    BASE_DIR=base_dir,
    APP_NAME=app_name,
    SITE_ID=SiteID(default=120),
    EDC_DX_LABELS=dict(hiv="HIV", dm="Diabetes", htn="Hypertension", chol="High Cholesterol"),
    EDC_DX_REVIEW_APP_LABEL="mocca_subject",
    EDC_PHQ9_MODEL_AT_BASELINE_ONLY=True,
    EDC_PHQ9_MODEL="mocca_subject.patienthealth",
    MOCCA_REGISTER_FILE=os.path.join(base_dir, "tests", "mocca_register.csv"),
    EDC_AUTH_SKIP_SITE_AUTHS=True,
    EDC_AUTH_SKIP_AUTH_UPDATER=True,
    EDC_SITES_MODULE_NAME="mocca_sites.sites",
    EDC_PROTOCOL_STUDY_OPEN_DATETIME=get_datetime_from_env(2019, 6, 30, 0, 0, 0, "UTC"),
    EDC_PROTOCOL_STUDY_CLOSE_DATETIME=get_datetime_from_env(2024, 12, 31, 23, 59, 59, "UTC"),
    ADVERSE_EVENT_ADMIN_SITE="mocca_ae_admin",
    ADVERSE_EVENT_APP_LABEL="mocca_ae",
    SUBJECT_SCREENING_MODEL=f"{app_name.replace('edc', 'screening')}.subjectscreening",
    SUBJECT_CONSENT_MODEL=f"{app_name.replace('edc', 'consent')}.subjectconsent",
    SUBJECT_VISIT_MODEL=f"{app_name.replace('edc', 'subject')}.subjectvisit",
    SUBJECT_VISIT_MISSED_MODEL=f"{app_name.replace('edc', 'subject')}.subjectvisitmissed",
    SUBJECT_REQUISITION_MODEL=f"{app_name.replace('edc', 'subject')}.subjectrequisition",
    SUBJECT_APP_LABEL=f"{app_name.replace('edc', 'subject')}",
    EDC_NAVBAR_DEFAULT="mocca_dashboard",
    DASHBOARD_BASE_TEMPLATES=dict(
        edc_base_template="edc_dashboard/base.html",
        listboard_base_template="mocca_edc/base.html",
        dashboard_base_template="mocca_edc/base.html",
        screening_listboard_template="mocca_dashboard/screening/listboard.html",
        subject_listboard_template="mocca_dashboard/subject/listboard.html",
        subject_dashboard_template="mocca_dashboard/subject/dashboard.html",
        subject_review_listboard_template="edc_review_dashboard/subject_review_listboard.html",
    ),
    ETC_DIR=os.path.join(base_dir, "tests", "etc"),
    EDC_BOOTSTRAP=3,
    EMAIL_BACKEND="django.core.mail.backends.locmem.EmailBackend",
    EMAIL_CONTACTS={
        "data_request": "someone@example.com",
        "data_manager": "someone@example.com",
    },
    EMAIL_ENABLED=True,
    HOLIDAY_FILE=join(base_dir, "tests", "holidays.csv"),
    LIVE_SYSTEM=False,
    EDC_RANDOMIZATION_LIST_PATH=join(base_dir, "tests", "etc"),
    EDC_RANDOMIZATION_REGISTER_DEFAULT_RANDOMIZER=False,
    DATABASES={
        # required for tests when acting as a server that deserializes
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(base_dir, "db.sqlite3"),
        },
    },
    INSTALLED_APPS=[
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
        "django.contrib.sites",
        "django_crypto_fields.apps.AppConfig",
        "django_revision.apps.AppConfig",
        "django_extensions",
        "django_celery_results",
        "django_celery_beat",
        "logentry_admin",
        "simple_history",
        "storages",
        "edc_action_item.apps.AppConfig",
        "edc_appointment.apps.AppConfig",
        "edc_adverse_event.apps.AppConfig",
        "edc_auth.apps.AppConfig",
        "edc_consent.apps.AppConfig",
        "edc_reportable.apps.AppConfig",
        "edc_crf.apps.AppConfig",
        "edc_lab.apps.AppConfig",
        "edc_visit_schedule.apps.AppConfig",
        "edc_dashboard.apps.AppConfig",
        "edc_data_manager.apps.AppConfig",
        "edc_device.apps.AppConfig",
        "edc_dx.apps.AppConfig",
        "edc_dx_review.apps.AppConfig",
        "edc_export.apps.AppConfig",
        "edc_facility.apps.AppConfig",
        "edc_fieldsets.apps.AppConfig",
        "edc_form_validators.apps.AppConfig",
        "edc_identifier.apps.AppConfig",
        "edc_lab_dashboard.apps.AppConfig",
        "edc_label.apps.AppConfig",
        "edc_list_data.apps.AppConfig",
        "edc_locator.apps.AppConfig",
        "edc_metadata.apps.AppConfig",
        "edc_model_admin.apps.AppConfig",
        "edc_model_wrapper.apps.AppConfig",
        "edc_navbar.apps.AppConfig",
        "edc_notification.apps.AppConfig",
        "edc_offstudy.apps.AppConfig",
        "edc_pharmacy.apps.AppConfig",
        "edc_pdutils.apps.AppConfig",
        "edc_protocol.apps.AppConfig",
        "edc_prn.apps.AppConfig",
        "edc_randomization.apps.AppConfig",
        "edc_reference.apps.AppConfig",
        "edc_registration.apps.AppConfig",
        "edc_reports.apps.AppConfig",
        "edc_review_dashboard.apps.AppConfig",
        "edc_sites.apps.AppConfig",
        "edc_subject_dashboard.apps.AppConfig",
        "edc_timepoint.apps.AppConfig",
        "edc_visit_tracking.apps.AppConfig",
        "edc_ltfu.apps.AppConfig",
        "mocca_consent.apps.AppConfig",
        "mocca_lists.apps.AppConfig",
        "mocca_dashboard.apps.AppConfig",
        "mocca_labs.apps.AppConfig",
        "mocca_subject.apps.AppConfig",
        "mocca_form_validators.apps.AppConfig",
        "mocca_visit_schedule.apps.AppConfig",
        "mocca_ae.apps.AppConfig",
        # "mocca_auth.apps.AppConfig",
        "mocca_prn.apps.AppConfig",
        "mocca_export.apps.AppConfig",
        "mocca_screening.apps.AppConfig",
        "mocca_sites.apps.AppConfig",
        "mocca_edc.apps.AppConfig",
    ],
    add_dashboard_middleware=True,
    add_lab_dashboard_middleware=True,
    add_adverse_event_dashboard_middleware=True,
).settings


def main():
    if not settings.configured:
        settings.configure(**DEFAULT_SETTINGS)
    django.setup()
    tags = [t.split("=")[1] for t in sys.argv if t.startswith("--tag")]
    failfast = True if [t for t in sys.argv if t == "--failfast"] else False
    failures = DiscoverRunner(failfast=failfast, tags=tags).run_tests(["tests"])
    sys.exit(bool(failures))


if __name__ == "__main__":
    logging.basicConfig()
    main()
