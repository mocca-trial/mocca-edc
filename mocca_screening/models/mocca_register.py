from django.core.validators import (
    RegexValidator,
    MinLengthValidator,
    MaxLengthValidator,
    MaxValueValidator,
    MinValueValidator,
)
from django.db import models
from django.db.models import Index, UniqueConstraint
from django_crypto_fields.fields import (
    EncryptedCharField,
    EncryptedTextField,
    FirstnameField,
    LastnameField,
)
from edc_constants.choices import ALIVE_DEAD_UNKNOWN, GENDER, YES_NO
from edc_constants.constants import NO, UNKNOWN, YES
from edc_model.models import BaseUuidModel, HistoricalRecords
from edc_sites import get_current_country
from edc_sites.models import CurrentSiteManager, SiteModelMixin
from edc_utils import get_utcnow
from mocca_lists.models import MoccaOriginalSites

from ..mocca_original_sites import get_mocca_site_limited_to


class Manager(models.Manager):
    """A manager class for Crf models, models that have an FK to
    the visit model.
    """

    use_in_migrations = True

    def get_by_natural_key(self, mocca_study_identifier):
        return self.get(mocca_study_identifier=mocca_study_identifier)


class MoccaRegister(SiteModelMixin, BaseUuidModel):

    report_datetime = models.DateTimeField(default=get_utcnow)

    screening_identifier = models.CharField(
        verbose_name="MOCCA (ext) screening identifier", max_length=15, null=True,
    )

    mocca_screening_identifier = models.CharField(
        verbose_name="MOCCA (original) screening identifier",
        max_length=15,
        null=True,
        blank=True,
        help_text="If known",
    )

    mocca_study_identifier = models.CharField(
        verbose_name="MOCCA (original) study identifier",
        max_length=25,
        validators=[
            RegexValidator(
                r"0[0-9]{1}\-0[0-9]{3}|[0-9]{6}",
                "Invalid format. Expected 12-3456 for UG, 123456 for TZ",
            )
        ],
        help_text="Format must match original identifier. e.g. 12-3456 for UG, 123456 for TZ",
    )

    mocca_country = models.CharField(
        max_length=25, choices=(("uganda", "Uganda"), ("tanzania", "Tanzania"))
    )

    mocca_site = models.ForeignKey(
        MoccaOriginalSites,
        on_delete=models.PROTECT,
        limit_choices_to=get_mocca_site_limited_to,
    )

    first_name = FirstnameField(null=True)

    last_name = LastnameField(null=True)

    initials = EncryptedCharField(
        validators=[
            RegexValidator("[A-Z]{1,3}", "Invalid format"),
            MinLengthValidator(2),
            MaxLengthValidator(3),
        ],
        help_text="Use UPPERCASE letters only. May be 2 or 3 letters.",
        null=True,
        blank=False,
    )
    gender = models.CharField(max_length=10, choices=GENDER, null=True, blank=False)

    age_in_years = models.IntegerField(
        validators=[MinValueValidator(18), MaxValueValidator(110)],
        null=True,
        blank=False,
    )

    birth_year = models.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2002)],
        null=True,
        blank=False,
    )
    dob = models.DateField(null=True, blank=True)

    survival_status = models.CharField(
        max_length=25, choices=ALIVE_DEAD_UNKNOWN, default=UNKNOWN
    )

    contact_attempts = models.IntegerField(default=0,)

    call = models.CharField(max_length=15, choices=YES_NO, default=YES)

    date_last_called = models.DateField(null=True)

    notes = EncryptedTextField(null=True, blank=True)

    on_site = CurrentSiteManager()
    objects = Manager()
    history = HistoricalRecords()

    def __str__(self):
        return f"{self.mocca_study_identifier} {self.initials} {self.age_in_years} {self.gender}"

    def natural_key(self):
        return (self.mocca_study_identifier,)

    natural_key.dependencies = [
        "sites.Site",
        "mocca_lists.MoccaOriginalSites",
    ]

    def save(self, *args, **kwargs):
        self.mocca_country = get_current_country()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "MOCCA Patient Register"
        verbose_name_plural = "MOCCA Patient Register"
        ordering = ["mocca_country", "mocca_site"]
        indexes = [
            Index(fields=["mocca_country", "mocca_site"]),
            Index(fields=["mocca_study_identifier", "initials", "gender"]),
        ]
        constraints = [
            UniqueConstraint(
                fields=["mocca_screening_identifier"],
                name="unique_mocca_screening_identifier",
            ),
            UniqueConstraint(
                fields=["mocca_study_identifier"], name="unique_mocca_study_identifier"
            ),
            # UniqueConstraint(
            #     fields=["first_name", "last_name"], name="unique_first_name__last_name"
            # ),
        ]
