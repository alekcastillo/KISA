# Generated by Django 3.0.7 on 2020-07-04 00:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20200627_0313'),
    ]

    operations = [
        migrations.AddField(
            model_name='busrouteticket',
            name='date_payed',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]