# Generated by Django 2.0.6 on 2018-07-12 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portalapp', '0012_auto_20180713_0020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='approval',
            field=models.IntegerField(),
        ),
    ]