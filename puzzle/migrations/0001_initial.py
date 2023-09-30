# Generated by Django 4.2.5 on 2023-09-29 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="puzzle",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nounce", models.PositiveIntegerField()),
                ("solution", models.CharField(max_length=250)),
                ("level", models.PositiveIntegerField()),
                ("data", models.CharField(max_length=250)),
            ],
        ),
    ]