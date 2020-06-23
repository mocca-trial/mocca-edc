from django.db import models
from edc_constants.choices import YES_NO
from edc_constants.constants import NO
from edc_crf.model_mixins import CrfModelMixin
from edc_model import models as edc_models


class Complications(CrfModelMixin, edc_models.BaseUuidModel):

    # stroke
    stroke = models.CharField(
        verbose_name="Stroke", max_length=25, choices=YES_NO, null=True, blank=True,
    )

    stroke_ago = edc_models.DurationYearMonthField(
        verbose_name="If YES, how long ago", null=True, blank=True,
    )

    stroke_estimated_date = models.DateField(
        verbose_name="Estimated date of stroke", null=True, blank=True, editable=False,
    )

    # heart_attack
    heart_attack = models.CharField(
        verbose_name="Heart attack / heart failure",
        max_length=25,
        choices=YES_NO,
        null=True,
        blank=True,
    )

    heart_attack_ago = edc_models.DurationYearMonthField(
        verbose_name="If yes, how long ago", null=True, blank=True,
    )

    heart_attack_estimated_date = models.DateField(
        verbose_name="Estimated date of heart attack / heart failure",
        null=True,
        blank=True,
        editable=False,
    )

    # renal
    renal_disease = models.CharField(
        verbose_name="Renal (kidney) disease",
        max_length=25,
        choices=YES_NO,
        null=True,
        blank=True,
    )

    renal_disease_ago = edc_models.DurationYearMonthField(
        verbose_name="If yes, how long ago", null=True, blank=True,
    )

    renal_disease_estimated_date = models.DateField(
        verbose_name="Estimated date of renal_disease",
        null=True,
        blank=True,
        editable=False,
    )
    # vision
    vision = models.CharField(
        verbose_name="Vision problems (e.g. blurred vision)",
        max_length=25,
        choices=YES_NO,
        null=True,
        blank=True,
    )

    vision_ago = edc_models.DurationYearMonthField(
        verbose_name="If yes, how long ago", null=True, blank=True,
    )

    vision_estimated_date = models.DateField(
        verbose_name="Estimated date of vision problems",
        null=True,
        blank=True,
        editable=False,
    )

    # numbness
    numbness = models.CharField(
        verbose_name="Numbness / burning sensation",
        max_length=25,
        choices=YES_NO,
        null=True,
        blank=True,
    )

    numbness_ago = edc_models.DurationYearMonthField(
        verbose_name="If yes, how long ago", null=True, blank=True,
    )

    numbness_estimated_date = models.DateField(
        verbose_name="Estimated date of numbness",
        null=True,
        blank=True,
        editable=False,
    )

    # foot ulcers
    foot_ulcers = models.CharField(
        verbose_name="Foot ulcers",
        max_length=25,
        choices=YES_NO,
        null=True,
        blank=True,
    )

    foot_ulcers_ago = edc_models.DurationYearMonthField(
        verbose_name="If yes, how long ago", null=True, blank=True,
    )

    foot_ulcers_estimated_date = models.DateField(
        verbose_name="Estimated date of foot ulcers",
        null=True,
        blank=True,
        editable=False,
    )
    #
    complications = models.CharField(
        verbose_name="Are there any other major complications to report?",
        max_length=25,
        choices=YES_NO,
        default=NO,
    )

    complications_other = models.TextField(
        null=True, blank=True, help_text="Please include dates",
    )

    def save(self, *args, **kwargs):
        complications = [
            "stroke_ago",
            "heart_attack",
            "renal_disease",
            "vision",
            "numbness",
            "foot_ulcers",
        ]
        for complication in complications:
            if getattr(self, complication, None):
                duration = edc_models.duration_to_date(
                    self.stroke_ago, self.report_datetime
                )
                setattr(self, f"{complication}_estimated_date", duration)
        super().save(*args, **kwargs)

    class Meta(CrfModelMixin.Meta, edc_models.BaseUuidModel.Meta):
        verbose_name = "Complications"
        verbose_name_plural = "Complications"
