from edc_reportable import site_reportables

# TODO: Verify
from edc_reportable.grading_data.daids_july_2017 import grading_data
from edc_reportable.normal_data.africa import normal_data

site_reportables.register(name="mocca", normal_data=normal_data, grading_data=grading_data)
