from django.db import models
from edc_blood_results.model_mixins import GlucoseModelMixin
from edc_constants.choices import YES_NO, YES_NO_NA
from edc_constants.constants import NOT_APPLICABLE
from edc_model import models as edc_models
from edc_model.models import date_not_future

from ..model_mixins import CrfModelMixin


class Glucose(GlucoseModelMixin, CrfModelMixin, edc_models.BaseUuidModel):

    glucose_performed = models.CharField(
        verbose_name=(
            "Has the patient had their glucose measured today or since the last visit?"
        ),
        max_length=15,
        choices=YES_NO,
    )

    # TODO: Copied from commented-out code in: edc_glucose/model_mixins/blood_glucose_model_mixin.py
    glucose_date = models.DateField(
        validators=[date_not_future],
        null=True,
        blank=True,
    )

    # TODO: Renamed fasting to glucose_fasted
    glucose_fasted = models.CharField(
        verbose_name="Has the participant fasted?",
        max_length=15,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE,
    )

    glucose = models.DecimalField(
        verbose_name="Glucose result",
        max_digits=8,
        decimal_places=2,
        null=True,
        blank=True,
    )

    class Meta(CrfModelMixin.Meta, edc_models.BaseUuidModel.Meta):
        verbose_name = "Glucose: Followup"
        verbose_name_plural = "Glucose: Followup"


class GlucoseBaseline(Glucose):
    class Meta:
        proxy = True
        verbose_name = "Glucose: Baseline"
        verbose_name_plural = "Glucose: Baseline"
