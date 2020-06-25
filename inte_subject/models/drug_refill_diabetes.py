from django.db import models
from edc_model import models as edc_models
from inte_lists.models import DiabetesTreatments

from ..model_mixins import CrfModelMixin, DrugRefillModelMixin


class DrugRefillDiabetes(DrugRefillModelMixin, CrfModelMixin, edc_models.BaseUuidModel):

    rx = models.ManyToManyField(
        DiabetesTreatments,
        verbose_name="Which medicine did the patient receive today?",
    )

    class Meta(CrfModelMixin.Meta, edc_models.BaseUuidModel.Meta):
        verbose_name = "Drug Refill: Diabetes"
        verbose_name_plural = "Drug Refills: Diabetes"
