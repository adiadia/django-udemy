# Generated by Django 2.2 on 2019-06-02 12:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20190602_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='helloworld',
            name='publish_date',
            field=models.DateField(default=datetime.datetime(2019, 6, 2, 12, 3, 44, 166953, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='helloworld',
            name='title',
            field=models.CharField(max_length=250, unique=True, verbose_name='Post Title'),
        ),
    ]