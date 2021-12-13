# Generated by Django 2.2.10 on 2021-12-09 14:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0014_auto_20211209_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 12, 9, 14, 42, 29, 210915, tzinfo=utc), editable=False),
        ),
        migrations.AlterField(
            model_name='answer',
            name='user',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]