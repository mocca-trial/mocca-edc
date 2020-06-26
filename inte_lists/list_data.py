from django.conf import settings
from edc_constants.constants import (
    DEAD,
    DIABETES,
    HIV,
    HYPERTENSION,
    LOST_TO_FOLLOWUP,
    OTHER,
    REFILL,
    ROUTINE_VISIT,
    UNWELL_VISIT,
)
from edc_list_data import PreloadData
from inte_prn.constants import (
    LATE_EXCLUSION,
    TRANSFERRED,
    WITHDRAWAL,
)

list_data = {
    "inte_lists.conditions": [
        (HYPERTENSION, "Patient has high blood pressure (Hypertension)"),
        (DIABETES, "Patient has high blood sugar (Diabetes)"),
        (HIV, "Patient has HIV infection (HIV+)"),
    ],
    "inte_lists.reasonsfortesting": [
        ("patient_request", "Patient was well and made a request"),
        ("patient_complication", "Patient had a clinical complication"),
        ("signs_symptoms", "Patient had suggestive signs and symptoms"),
        (OTHER, "Other reason (specify below)"),
    ],
    "inte_lists.offstudyreasons": [
        ("completed_followup", "Patient completed 12 months of follow-up"),
        (LOST_TO_FOLLOWUP, "Patient lost to follow-up"),
        (DEAD, "Patient reported/known to have died"),
        (WITHDRAWAL, "Patient withdrew consent to participate further"),
        (LATE_EXCLUSION, "Patient fulfilled late exclusion criteria*"),
        (TRANSFERRED, "Patient has been transferred to another health centre"),
        (OTHER, "Other reason (specify below)",),
    ],
    "inte_lists.hypertensiontreatments": [
        ("amlodipine", "Amlodipine"),
        ("atenolol", "Atenolol"),
        ("bendroflumethiazide", "Bendroflumethiazide"),
        ("captopril", "Captopril"),
        ("carvedilol", "Carvedilol"),
        ("enalapril", "Enalapril"),
        ("frusemide", "Frusemide"),
        ("losartan", "Losartan"),
        ("metoprolol", "Metoprolol"),
        ("nifedipine", "Nifedipine"),
        ("ramipril", "Ramipril"),
        ("simvastatin", "Simvastatin"),
        ("valsartan", "Valsartan"),
        (OTHER, "Other treatment (specify below)"),
    ],
    "inte_lists.arvregimens": [
        ("ABC_3TC_DTG", "ABC + 3TC + DTG"),
        ("ABC_3TC_EFV", "ABC + 3TC + EFV"),
        ("AZT_3TC_DTG", "AZT + 3TC + DTG"),
        ("AZT_3TC_EFV", "AZT + 3TC + EFV"),
        ("AZT_3TC_NVP", "AZT + 3TC + NVP"),
        ("TDF_3TC_DTG", "TDF + 3TC + DTG"),
        ("TDF_3TC_EFV", "TDF + 3TC + EFV"),
        ("TDF_3TC_NVP", "TDF + 3TC + NVP"),
        ("TDF_FTC_DTG", "TDF + FTC + DTG"),
        ("TDF_FTC_EFV", "TDF + FTC + EFV"),
        ("TDF_FTC_NVP", "TDF + FTC + NVP"),
        ("ABC_3TC_ATV_r", "ABC + 3TC + ATV/r"),
        ("ABC_3TC_LPV_r", "ABC + 3TC + LPV/r"),
        ("AZT_3TC_ATV_r", "AZT + 3TC + ATV/r"),
        ("AZT_3TC_LPV_r", "AZT + 3TC + LPV/r"),
        ("DTG_ABC/3TC_ATV_r", "DTG + (ABC/3TC) + ATV/r"),
        ("TDF_3TC_ATV_r", "TDF + 3TC + ATV/r"),
        ("TDF_3TC_LPV_r", "TDF + 3TC + LPV/r"),
        ("TDF_FTC_ATV_r", "TDF + FTC + ATV/r"),
        ("TDF_FTC_LPV_r", "TDF + FTC + LPV/r"),
        (OTHER, "Other, specify"),
    ],
    "inte_lists.arvdrugs": [
        ("3TC", "3TC"),
        ("ABC", "ABC"),
        ("ATV_r", "ATV/r"),
        ("AZT", "AZT"),
        ("DTG", "DTG"),
        ("EFV", "EFV"),
        ("FTC", "FTC"),
        ("LPV_r", "LPV/r"),
        ("NVP", "NVP"),
        ("TDF", "TDF"),
        (OTHER, "Other, specify"),
    ],
    "inte_lists.visitreasons": [
        ("drug_refill", "Drug Refill"),
        ("clinic_review", "Clinic Review"),
        ("unwell", "Feeling unwell (self referral)"),
        ("unscheduled", "Unscheduled"),
    ],
    "inte_lists.diabetestreatments": [
        ("glibenclamide_s", "Glibenclamide (S)"),
        ("gliclazide_s", "Gliclazide (S)"),
        ("glimepiride_s", "Glimepiride (S)"),
        ("glipizide_s", "Glipizide (S)"),
        ("insulin", "Insulin"),
        ("metformin_b", "Metformin (B)"),
        (OTHER, "Other, specify"),
    ],
    "inte_lists.healthservices": [
        (HYPERTENSION, "Hypertension"),
        (DIABETES, "Diabetes"),
        (HIV, "HIV"),
    ],
    "inte_lists.clinicservices": [
        (REFILL, "Drug refill"),
        (ROUTINE_VISIT, "Routine clinic review by a clinician"),
        (UNWELL_VISIT, "Feeling unwell"),
        (OTHER, "Other, specify"),
    ],
    "inte_lists.rxmodifications": [
        ("dose_changes", "Dose changes"),
        ("drugs_substitution", "Drugs substitution"),
        ("drug_additions", "Additional drugs added to existing regimen"),
        ("some_stopped", "Some drugs stopped"),
        (OTHER, "Other, specify"),
    ],
    "inte_lists.rxmodificationreasons": [
        ("availability", "Limited availability of drugs"),
        ("side_effects", "Had side-effects"),
        ("feel_better", "Felt well and stopped/reduced drug prescription"),
        (OTHER, "Other, specify"),
    ],
}

if settings.APP_NAME != "inte_lists":
    preload_data = PreloadData(list_data=list_data)
