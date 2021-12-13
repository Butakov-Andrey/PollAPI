# Generated by Django 2.2.10 on 2021-12-09 14:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0012_auto_20211209_1659'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='choice',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='value',
        ),
        migrations.AddField(
            model_name='answer',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 12, 9, 14, 39, 2, 552552, tzinfo=utc), editable=False),
        ),
        migrations.AddField(
            model_name='answer',
            name='text',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
    ]