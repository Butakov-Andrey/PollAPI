# Generated by Django 2.2.10 on 2021-12-09 15:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0015_auto_20211209_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 9, 15, 7, 55, 690064, tzinfo=utc), editable=False),
        ),
    ]
