# Generated by Django 4.2.1 on 2023-05-30 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="InnovateModel",
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
                ("name", models.CharField(max_length=150)),
                ("department", models.CharField(max_length=150)),
                ("title", models.CharField(max_length=150)),
                ("description", models.CharField(max_length=300)),
                ("benefits", models.CharField(max_length=300)),
                ("plan", models.CharField(max_length=150)),
            ],
        ),
    ]