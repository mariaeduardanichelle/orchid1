# Generated by Django 4.1 on 2022-08-30 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_origen_delete_categoria"),
    ]

    operations = [
        migrations.AlterField(
            model_name="origen",
            name="poder",
            field=models.CharField(max_length=1000000),
        ),
    ]
