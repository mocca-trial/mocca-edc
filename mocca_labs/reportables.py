from edc_reportable import site_reportables
from respond_model.labs.reportables import grading_data, normal_data

site_reportables.register(name="mocca", normal_data=normal_data, grading_data=grading_data)
