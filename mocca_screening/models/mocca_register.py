from django.core.validators import (
    RegexValidator,
    MinLengthValidator,
    MaxLengthValidator,
    MaxValueValidator,
    MinValueValidator,
)
from django.db import models
from django.db.models import Index, PROTECT
from django_crypto_fields.fields import (
    EncryptedCharField,
    FirstnameField,
    LastnameField,
)
from edc_constants.choices import ALIVE_DEAD_UNKNOWN, GENDER, YES_NO
from edc_constants.constants import NO, UNKNOWN
from edc_model.models import BaseUuidModel
from edc_utils import get_utcnow
from mocca_lists.models import MoccaOriginalSites


class MoccaRegister(BaseUuidModel):

    mocca_screening_identifier = models.CharField(max_length=15)

    mocca_study_identifier = models.CharField(max_length=15)

    mocca_country = models.CharField(
        max_length=25, choices=(("uganda", "Uganda"), ("tanzania", "Tanzania"))
    )

    mocca_site = models.ForeignKey(MoccaOriginalSites, on_delete=models.PROTECT)

    first_name = FirstnameField()

    last_name = LastnameField()

    initials = EncryptedCharField(
        validators=[
            RegexValidator("[A-Z]{1,3}", "Invalid format"),
            MinLengthValidator(2),
            MaxLengthValidator(3),
        ],
        help_text="Use UPPERCASE letters only. May be 2 or 3 letters.",
        blank=False,
    )
    gender = models.CharField(max_length=10, choices=GENDER,)

    age_in_years = models.IntegerField(
        validators=[MinValueValidator(18), MaxValueValidator(110)]
    )

    dob = models.DateField()

    # survival_status = models.CharField(
    #     max_length=25, choices=ALIVE_DEAD_UNKNOWN, default=UNKNOWN
    # )

    def __str__(self):
        return self.mocca_study_identifier

    class Meta:
        verbose_name = "MOCCA Patient Register"
        verbose_name_plural = "MOCCA Patient Register"
        ordering = ["mocca_country", "mocca_site"]
        indexes = [
            Index(fields=["mocca_country", "mocca_site"]),
            Index(fields=["mocca_study_identifier", "initials", "gender"]),
        ]


class MoccaRegisterContact(BaseUuidModel):

    mocca_register = models.ForeignKey(MoccaRegister, on_delete=PROTECT)

    report_datetime = models.DateTimeField(default=get_utcnow)

    contacted = models.CharField(max_length=15, choices=YES_NO, default=NO)

    class Meta:
        verbose_name = "MOCCA Patient Register Contact"
        verbose_name_plural = "MOCCA Patient Register Contacts"
