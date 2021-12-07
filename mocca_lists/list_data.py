from edc_constants.constants import (
    DEAD,
    DIABETES,
    FREE_OF_CHARGE,
    HIV,
    HOSPITALIZED,
    HYPERTENSION,
    NOT_APPLICABLE,
    OTHER,
    REFILL,
    ROUTINE_VISIT,
    STUDY_DEFINED_TIMEPOINT,
    UNKNOWN,
    UNWELL_VISIT,
)
from edc_ltfu.constants import LOST_TO_FOLLOWUP
from edc_offstudy.constants import LATE_EXCLUSION, WITHDRAWAL
from edc_transfer.constants import TRANSFERRED

list_data = {
    "mocca_lists.diagnosislocations": [
        ("hospital", "Hospital"),
        ("gov_clinic", "Government clinic"),
        ("private_clinic", "Private clinic"),
        ("private_doctor", "Private doctor"),
        ("mocca_clinic", "MOCCA study clinic"),
        (UNKNOWN, "Don't recall"),
        (OTHER, "Other, specify"),
    ],
    "mocca_lists.moccaoriginalsites": [
        ("amana", "Amana"),
        ("bunju", "Bunju"),
        ("hindu_mandal", "Hindu Mandal"),
        ("mkuranga", "Mkuranga"),
        ("mwananyamala", "Mwananyamala"),
        ("kisugu", "Kisugu"),
        ("kiswa", "Kiswa"),
        ("mulago", "Mulago"),
        ("ndejje", "Ndejje"),
        ("wakiso", "Wakiso"),
    ],
    "mocca_lists.conditions": [
        (HYPERTENSION, "Patient has high blood pressure (Hypertension)"),
        (DIABETES, "Patient has high blood sugar (Diabetes)"),
        (HIV, "Patient has HIV infection (HIV+)"),
    ],
    "mocca_lists.refillconditions": [
        (HYPERTENSION, "Hypertension"),
        (DIABETES, "Diabetes"),
        (HIV, "HIV"),
    ],
    "mocca_lists.reasonsfortesting": [
        ("patient_request", "Patient was well and made a request"),
        ("patient_complication", "Patient had a clinical complication"),
        ("signs_symptoms", "Patient had suggestive signs and symptoms"),
        (OTHER, "Other reason (specify below)"),
    ],
    "mocca_lists.offstudyreasons": [
        ("completed_followup", "Patient completed 12 months of follow-up"),
        (LOST_TO_FOLLOWUP, "Patient lost to follow-up"),
        (DEAD, "Patient reported/known to have died"),
        (WITHDRAWAL, "Patient withdrew consent to participate further"),
        (LATE_EXCLUSION, "Patient fulfilled late exclusion criteria*"),
        (TRANSFERRED, "Patient has been transferred to another health centre"),
        (
            OTHER,
            "Other reason (specify below)",
        ),
    ],
    "mocca_lists.htntreatments": [
        ("aldactone", "Aldactone (Spironolactone)"),
        ("amlodipine", "Amlodipine"),
        ("atenolol", "Atenolol"),
        ("atorvastatin", "Atorvastatin"),
        ("bendroflumethiazide", "Bendroflumethiazide"),
        ("bisoprolol", "Bisoprolol"),
        ("captopril", "Captopril"),
        ("carvedilol", "Carvedilol"),
        ("clopidogrel", "Clopidogrel"),
        ("enalapril", "Enalapril"),
        ("frusemide", "Frusemide"),
        ("hydralazine", "Hydralazine"),
        ("hydrochlorothiazide", "Hydrochlorothiazide"),
        ("junior_aspirin", "Junior Aspirin"),
        ("losartan_h", "losartan Hydrochlorothiazide (Losartan H/Repace H)"),
        ("losartan", "losartan"),
        ("metoprolol", "Metoprolol"),
        ("nifedipine", "Nifedipine"),
        ("propanolol", "Propanolol"),
        ("ramipril", "Ramipril"),
        ("simvastatin", "Simvastatin"),
        ("valsartan", "Valsartan"),
        (OTHER, "Other treatment (specify below)"),
    ],
    "mocca_lists.arvregimens": [
        ("ABC_3TC_ATV_r", "ABC + 3TC + ATV/r"),
        ("ABC_3TC_DTG", "ABC + 3TC + DTG"),
        ("ABC_3TC_EFV", "ABC + 3TC + EFV"),
        ("ABC_3TC_LPV_r", "ABC + 3TC + LPV/r"),
        ("AZT_3TC_ATV_r", "AZT + 3TC + ATV/r"),
        ("AZT_3TC_DTG", "AZT + 3TC + DTG"),
        ("AZT_3TC_EFV", "AZT + 3TC + EFV"),
        ("AZT_3TC_LPV_r", "AZT + 3TC + LPV/r"),
        ("AZT_3TC_NVP", "AZT + 3TC + NVP"),
        ("DTG_ABC/3TC_ATV_r", "DTG + (ABC/3TC) + ATV/r"),
        ("TDF_3TC_ATV_r", "TDF + 3TC + ATV/r"),
        ("TDF_3TC_DTG", "TDF + 3TC + DTG"),
        ("TDF_3TC_EFV", "TDF + 3TC + EFV"),
        ("TDF_3TC_LPV_r", "TDF + 3TC + LPV/r"),
        ("TDF_3TC_NVP", "TDF + 3TC + NVP"),
        ("TDF_FTC_ATV_r", "TDF + FTC + ATV/r"),
        ("TDF_FTC_DTG", "TDF + FTC + DTG"),
        ("TDF_FTC_EFV", "TDF + FTC + EFV"),
        ("TDF_FTC_LPV_r", "TDF + FTC + LPV/r"),
        ("TDF_FTC_NVP", "TDF + FTC + NVP"),
        (OTHER, "Other, specify"),
    ],
    "mocca_lists.arvdrugs": [
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
    "mocca_lists.visitreasons": [
        ("drug_refill", "Drug Refill"),
        ("clinic_review", "Clinic Review"),
        ("unwell", "Feeling unwell (self referral)"),
        ("unscheduled", "Unscheduled"),
    ],
    "mocca_lists.dmtreatments": [
        ("glibenclamide_metformin", "Glibenclamide + Metformin combo"),
        ("glibenclamide_s", "Glibenclamide (S)"),
        ("gliclazide_s", "Gliclazide (S)"),
        ("glimepiride_1mg_metformin", "Glimepiride (1mg) + Metformin combo"),
        ("glimepiride_2mg_metformin", "Glimepiride (2mg) + Metformin combo"),
        ("glimepiride_s", "Glimepiride (S)"),
        ("glipizide_s", "Glipizide (S)"),
        ("insulin", "Insulin"),
        ("metformin_b", "Metformin (B)"),
        ("pioglitazone", "Pioglitazone"),
        ("pregabalin", "Pregabalin (diabetic neuropathy)"),
        (
            "vitamin_b_folic_acid",
            "Vitamin Bs + Folic Acid (Neuroton- diabetic neuropathy)",
        ),
        (OTHER, "Other, specify"),
    ],
    "mocca_lists.choltreatments": [
        ("rosuvastatin", "Rosuvastatin"),
        ("simvastatin", "Simvastatin"),
        ("atorvastatin", "Atorvastatin"),
        (OTHER, "Other, specify"),
    ],
    "mocca_lists.clinicservices": [
        (STUDY_DEFINED_TIMEPOINT, "Scheduled study visit"),
        (ROUTINE_VISIT, "Routine clinic review by a clinician"),
        (REFILL, "Drug refill"),
        (UNWELL_VISIT, "Feeling unwell"),
        ("club_or_health_activity", "Patient club / Health Activity"),
        (NOT_APPLICABLE, "Not applicable"),
        (OTHER, "Other, specify"),
    ],
    "mocca_lists.rxmodifications": [
        ("dose_changes", "Dose changes"),
        ("drugs_substitution", "Drugs substitution"),
        ("drug_additions", "Additional drugs added to existing regimen"),
        ("some_stopped", "Some drugs stopped"),
        (OTHER, "Other, specify"),
    ],
    "mocca_lists.rxmodificationreasons": [
        ("availability", "Limited availability of drugs"),
        ("side_effects", "Had side-effects"),
        ("feel_better", "Felt well and stopped/reduced drug prescription"),
        (OTHER, "Other, specify"),
    ],
    "mocca_lists.subjectvisitmissedreasons": [
        ("forgot", "Forgot / Can’t remember being told about appointment"),
        ("family_emergency", "Family emergency (e.g. funeral) and was away"),
        ("travelling", "Away travelling/visiting"),
        ("working_schooling", "Away working/schooling"),
        ("too_sick", "Too sick or weak to come to the centre"),
        ("lack_of_transport", "Transportation difficulty"),
        (HOSPITALIZED, "Hospitalized"),
        (OTHER, "Other reason (specify below)"),
    ],
    "mocca_lists.drugpaysources": [
        ("own_cash", "Own cash"),
        ("insurance", "Insurance"),
        ("club", "Patient support group / club"),
        ("relative", "Relative or others paying"),
        (FREE_OF_CHARGE, "Free drugs from the pharmacy"),
        (OTHER, "Other pay source (specify below)"),
    ],
    "mocca_lists.transportchoices": [
        ("bus", "Bus"),
        ("train", "Train"),
        ("ambulance", "Ambulance"),
        ("private_taxi", "Private taxi"),
        ("own_bicycle", "Own bicycle"),
        ("hired_motorbike", "Hired motorbike"),
        ("own_car", "Own car"),
        ("own_motorbike", "Own motorbike"),
        ("hired_bicycle", "Hired bicycle"),
        ("foot", "Foot"),
        (OTHER, "Other reason (specify below)"),
    ],
    "mocca_lists.nonadherencereasons": [
        ("forgot_to_take", "I simply forgot to take my medication"),
        ("travelled", "I travelled and forgot my medication"),
        ("feel_better", "I felt better and stopped taking my medication"),
        (
            "insufficient_supply",
            "I did not get enough medication from hospital/clinic, could not buy more",
        ),
        ("feel_ill", "The medications were making me feel sick"),
        ("too_many_pills", "Too many pills so I stopped / reduced"),
        (OTHER, "Other, please specify ..."),
    ],
}

# preload_data = PreloadData(list_data=list_data)
