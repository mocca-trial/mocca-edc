from edc_clinic.models import MedicationAdherenceModelMixin
from edc_crf.model_mixins import CrfModelMixin
from edc_model import models as edc_models


class HtnMedicationAdherence(
    MedicationAdherenceModelMixin, CrfModelMixin, edc_models.BaseUuidModel
):
    class Meta(CrfModelMixin.Meta, edc_models.BaseUuidModel.Meta):
        verbose_name = "Hypertension Medication Adherence"
        verbose_name_plural = "Hypertension Medication Adherence"
