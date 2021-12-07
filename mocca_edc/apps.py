from dateutil.relativedelta import FR, MO, SA, SU, TH, TU, WE
from django.apps import AppConfig as DjangoAppConfig
from django.core.management.color import color_style
from django.db.backends.signals import connection_created
from edc_facility.apps import AppConfig as BaseEdcFacilityAppConfig
from edc_utils.sqlite import activate_foreign_keys

style = color_style()


# TODO: Verify ok?
# def post_migrate_update_edc_auth(sender=None, **kwargs):
#     from mocca_auth.codenames_by_group import get_codenames_by_group
#
#     GroupUpdater(groups=get_codenames_by_group(), verbose=True, apps=django_apps)


class AppConfig(DjangoAppConfig):
    name = "mocca_edc"

    def ready(self):
        # TODO: Verify ok?
        # post_migrate.connect(post_migrate_update_edc_auth, sender=self)

        # for sqlite only
        connection_created.connect(activate_foreign_keys)


class AppConfigForTests(DjangoAppConfig):
    name = "mocca_edc"


class EdcFacilityAppConfig(BaseEdcFacilityAppConfig):
    definitions = {
        "7-day-clinic": dict(
            days=[MO, TU, WE, TH, FR, SA, SU], slots=[100, 100, 100, 100, 100, 100, 100]
        ),
        "6-day-clinic": dict(
            days=[MO, TU, WE, TH, FR, SA], slots=[100, 100, 100, 100, 100, 100]
        ),
        "5-day-clinic": dict(days=[MO, TU, WE, TH, FR], slots=[100, 100, 100, 100, 100]),
        "4-day-clinic": dict(days=[MO, TU, WE, TH], slots=[100, 100, 100, 100]),
    }
