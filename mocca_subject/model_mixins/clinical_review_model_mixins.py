# from respond_model.model_mixins import (
#     ClinicalReviewModelMixin as BaseClinicalReviewModelMixin,
# )
# from respond_model.stubs import ClinicalReviewModelStub
#
#
# class ClinicalReviewModelMixin(BaseClinicalReviewModelMixin):
#
#     condition_labels = dict(hiv="HIV", htn="Hypertension", dm="Diabetes", chol="Cholesterol")
#
#     def get_best_chol_test_date(self: ClinicalReviewModelStub):
#         return self.chol_test_date or self.chol_test_estimated_datetime
#
#     @property
#     def diagnoses(self: ClinicalReviewModelStub) -> dict:
#         return {k: getattr(self, f"{k}_dx") for k in self.condition_labels}
#         # return dict(hiv=self.hiv_dx, htn=self.htn_dx, dm=self.dm_dx, chol=self.chol.dx)
#
#     @property
#     def diagnoses_labels(self) -> dict:
#         return self.condition_labels
#
#     class Meta:
#         abstract = True
