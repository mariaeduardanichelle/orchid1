# Generated by Django 4.1 on 2022-08-30 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Origen",
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
                ("nome", models.CharField(max_length=100)),
                ("descricao", models.CharField(max_length=100)),
                ("pericias_treinadas", models.CharField(max_length=100)),
                ("poder", models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name="Categoria",
        ),
    ]
