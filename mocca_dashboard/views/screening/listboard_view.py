import re

from django.db.models import Q
from django.urls import reverse
from edc_constants.constants import ABNORMAL
from edc_dashboard.view_mixins import (
    EdcViewMixin,
    ListboardFilterViewMixin,
    SearchFormViewMixin,
)
from edc_dashboard.views import ListboardView
from edc_navbar import NavbarViewMixin

from ...model_wrappers import SubjectScreeningModelWrapper
from .filters import ListboardViewFilters


class ListboardView(
    EdcViewMixin,
    NavbarViewMixin,
    ListboardFilterViewMixin,
    SearchFormViewMixin,
    ListboardView,
):

    listboard_template = "screening_listboard_template"
    listboard_url = "screening_listboard_url"
    listboard_panel_style = "info"
    listboard_fa_icon = "fa-user-plus"
    listboard_view_filters = ListboardViewFilters()
    listboard_model = "mocca_screening.subjectscreening"
    listboard_view_permission_codename = "edc_dashboard.view_screening_listboard"

    alternate_search_attr = "screening_identifier"

    model_wrapper_cls = SubjectScreeningModelWrapper
    navbar_selected_item = "screened_subject"
    ordering = "-report_datetime"
    paginate_by = 10
    search_form_url = "screening_listboard_url"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        url = reverse("mocca_screening_admin:mocca_screening_moccaregister_changelist")
        context.update(
            subject_screening_add_url=url,
            ABNORMAL=ABNORMAL,
        )
        return context

    def get_subject_screening_add_url(self):
        return self.listboard_model_cls().get_absolute_url()

    def get_queryset_filter_options(self, request, *args, **kwargs):
        options = super().get_queryset_filter_options(request, *args, **kwargs)
        if kwargs.get("screening_identifier"):
            options.update({"screening_identifier": kwargs.get("screening_identifier")})
        return options

    def extra_search_options(self, search_term):
        q_objects = []
        if re.match("^[A-Z\-]+$", search_term):
            q_objects.append(Q(initials__exact=search_term.upper()))
            q_objects.append(
                Q(screening_identifier__icontains=search_term.replace("-", "").upper())
            )
        if re.match("^[0-9]+$", search_term):
            q_objects.append(Q(hospital_identifier__exact=search_term))
        return q_objects
