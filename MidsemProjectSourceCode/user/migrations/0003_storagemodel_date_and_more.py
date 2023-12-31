# Generated by Django 4.2.4 on 2023-10-19 17:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0002_storagemodel"),
    ]

    operations = [
        migrations.AddField(
            model_name="storagemodel",
            name="DATE",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name="storagemodel",
            name="MOVEMENT_REACTION",
            field=models.DecimalField(decimal_places=10, max_digits=10),
        ),
        migrations.AlterField(
            model_name="storagemodel",
            name="POTENTIAL",
            field=models.DecimalField(decimal_places=10, max_digits=10),
        ),
        migrations.AlterField(
            model_name="storagemodel",
            name="RELEASE_CLAUSE_EUR",
            field=models.DecimalField(decimal_places=10, max_digits=10),
        ),
        migrations.AlterField(
            model_name="storagemodel",
            name="VALUE_EUR",
            field=models.DecimalField(decimal_places=10, max_digits=10),
        ),
    ]
