# Generated by Django 4.2.6 on 2023-10-21 18:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0005_alter_storagemodel_age_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="storagemodel",
            name="CONFIDENCE",
            field=models.FloatField(blank=True, default=0, verbose_name="CONFIDENCE"),
        ),
    ]