# Generated by Django 4.0.2 on 2022-02-18 15:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_information_balance_alter_information_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='information',
            name='birthday',
            field=models.DateTimeField(default=datetime.date(2022, 2, 18)),
        ),
    ]
