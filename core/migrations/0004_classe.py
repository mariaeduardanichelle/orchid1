# Generated by Django 4.1 on 2022-08-30 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_alter_origen_poder"),
    ]

    operations = [
        migrations.CreateModel(
            name="Classe",
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
            ],
        ),
    ]
