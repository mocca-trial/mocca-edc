from edc_model import models as edc_models
from respond_model.model_mixins.medication_model_mixins import (
    CholMedicationsModelMixin,
    DmMedicationsModelMixin,
    HivMedicationsModelMixin,
    HtnMedicationsModelMixin,
)

from ..model_mixins import CrfModelMixin


class Medications(
    HivMedicationsModelMixin,
    HtnMedicationsModelMixin,
    DmMedicationsModelMixin,
    CholMedicationsModelMixin,
    CrfModelMixin,
    edc_models.BaseUuidModel,
):
    class Meta(CrfModelMixin.Meta, edc_models.BaseUuidModel.Meta):
        verbose_name = "Medications"
        verbose_name_plural = "Medications"
