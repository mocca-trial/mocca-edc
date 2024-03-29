# Generated by Django 3.0.9 on 2020-12-04 00:30

import django_crypto_fields.fields.encrypted_text_field
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("mocca_screening", "0009_auto_20201204_0323"),
    ]

    operations = [
        migrations.AddField(
            model_name="historicalmoccaregister",
            name="notes",
            field=django_crypto_fields.fields.encrypted_text_field.EncryptedTextField(
                blank=True,
                help_text=" (Encryption: AES local)",
                max_length=71,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="moccaregister",
            name="notes",
            field=django_crypto_fields.fields.encrypted_text_field.EncryptedTextField(
                blank=True,
                help_text=" (Encryption: AES local)",
                max_length=71,
                null=True,
            ),
        ),
    ]
