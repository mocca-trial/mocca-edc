from django.core.exceptions import ObjectDoesNotExist
from django.template.loader import render_to_string
from django.urls import reverse
from edc_constants.constants import DEAD, NO
from edc_dashboard import url_names

from mocca_screening.models import (
    CareStatus,
    MoccaRegisterContact,
    SubjectRefusalScreening,
    SubjectScreening,
)
from mocca_screening.models.model_mixins import CareModelMixin


class ScreeningButton:
    """A class to render a screening button for the MoccaRegister
    changelist.

    Usage:
        screening_button = ScreeningButton(...)
        screening_button.rendered
    """

    template = "mocca_screening/bootstrap3/dashboard_button.html"
    screening_listboard_url_name = "screening_listboard_url"
    screening_add_url_name = "mocca_screening_admin:mocca_screening_subjectscreening_add"

    def __init__(
        self,
        mocca_register,
        changelist_url_name=None,
    ):
        self._last_mocca_register_contact = None
        self.mocca_register = mocca_register
        self.screening_listboard_url = url_names.get(self.screening_listboard_url_name)
        self.screening_listboard_url_kwargs = dict(
            screening_identifier=self.mocca_register.screening_identifier
        )
        self.screening_add_url = reverse(self.screening_add_url_name)
        self.changelist_url_name = changelist_url_name

    def __repr__(self):
        return f"{self.__class__.__name__}({self.mocca_register}, ...)"

    def __str__(self):
        return self.rendered

    @property
    def rendered(self):
        if self.context:
            return render_to_string(
                self.template,
                context={"title": f"{SubjectScreening._meta.verbose_name}", **self.context},
            )
        return None

    @property
    def context(self):
        """Returns the template context for the screening button
        or None.
        """
        mocca_register_contact = self.last_mocca_register_contact
        if self.mocca_register.screening_identifier:
            context = dict(**self.change_button_context)
        elif self.subject_refusal_screening:
            context = None
        elif not mocca_register_contact and self.mocca_register.subject_present == NO:
            context = None
        elif getattr(mocca_register_contact, "survival_status", "") == DEAD:
            context = None
        else:
            context = dict(**self.add_button_context)
        return context

    @property
    def last_mocca_register_contact(self):
        if not self._last_mocca_register_contact:
            self._last_mocca_register_contact = (
                MoccaRegisterContact.objects.filter(mocca_register=self.mocca_register)
                .order_by("created")
                .last()
            )
        return self._last_mocca_register_contact

    @property
    def subject_refusal_screening(self):
        """Returns a subject screening refusal instance or None"""
        try:
            return SubjectRefusalScreening.objects.get(mocca_register=self.mocca_register)
        except ObjectDoesNotExist:
            return None

    @property
    def add_button_context(self):
        """Returns a dictionary of additional context for the button
        if adding a model instance.
        """
        return dict(
            url="&".join([x for x in [self.add_url, self.care_status_query_string] if x]),
            label="Add",
            fa_icon="fas fa-plus",
            fa_icon_after=None,
            button_type="add",
        )

    @property
    def change_button_context(self):
        """Returns a dictionary of additional context for the button
        if editing the model instance.
        """
        return dict(
            url=reverse(
                self.screening_listboard_url,
                kwargs=self.screening_listboard_url_kwargs,
            ),
            label=self.mocca_register.screening_identifier,
            fa_icon="fas fa-share",
            fa_icon_after=True,
            button_type="go",
        )

    @property
    def add_url(self):
        """Returns an add url with querystring"""
        return (
            f"{self.screening_add_url}?next={self.changelist_url_name}"
            f"&mocca_register={str(self.mocca_register.id)}"
        )

    @property
    def care_status_query_string(self):
        """Return a querystring of carestatus fields=values"""
        try:
            care_status = CareStatus.objects.get(mocca_register=self.mocca_register)
        except ObjectDoesNotExist:
            query_string = None
        else:
            query_string = "&".join(
                [
                    f"{f}={getattr(care_status, f) or ''}"
                    for f in [f.name for f in CareModelMixin._meta.fields]
                ]
            )
        return query_string
