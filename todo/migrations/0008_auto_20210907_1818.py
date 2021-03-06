# Generated by Django 3.2.6 on 2021-09-07 12:33

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todo', '0007_alter_task_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='task',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 7, 18, 16, 31, 933256)),
        ),
    ]
