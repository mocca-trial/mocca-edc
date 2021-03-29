from django.db import models
from edc_constants.constants import NOT_APPLICABLE
from edc_model import models as edc_models
from respond_model.model_mixins import ReviewModelMixin

from ..choices import CHOL_MANAGEMENT
from ..model_mixins import CrfModelMixin


class CholReview(ReviewModelMixin, CrfModelMixin, edc_models.BaseUuidModel):

    managed_by = models.CharField(
        verbose_name="How will the patient's High Cholesterol be managed going forward?",
        max_length=25,
        choices=CHOL_MANAGEMENT,
        default=NOT_APPLICABLE,
    )

    class Meta(CrfModelMixin.Meta, edc_models.BaseUuidModel.Meta):
        verbose_name = "High Cholesterol Review"
        verbose_name_plural = "High Cholesterol Review"
