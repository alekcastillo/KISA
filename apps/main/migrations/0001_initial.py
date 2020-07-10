# Generated by Django 3.0.7 on 2020-07-10 17:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BusRoute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField()),
                ('updated_date', models.DateTimeField()),
                ('deleted_date', models.DateTimeField(blank=True, db_index=True, null=True)),
                ('title', models.CharField(max_length=80)),
                ('ticket_price', models.FloatField()),
                ('ctp_code', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField()),
                ('updated_date', models.DateTimeField()),
                ('deleted_date', models.DateTimeField(blank=True, db_index=True, null=True)),
                ('birth_date', models.DateField()),
                ('last_login_date', models.DateField()),
                ('balance', models.FloatField(default=0.0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField()),
                ('updated_date', models.DateTimeField()),
                ('deleted_date', models.DateTimeField(blank=True, db_index=True, null=True)),
                ('name', models.CharField(max_length=80)),
                ('province', models.IntegerField(choices=[(1, 'San Jose'), (2, 'Alajuela'), (3, 'Cartago'), (4, 'Heredia'), (5, 'Guanacaste'), (6, 'Puntarenas'), (7, 'Limon')])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField()),
                ('updated_date', models.DateTimeField()),
                ('deleted_date', models.DateTimeField(blank=True, db_index=True, null=True)),
                ('card_number', models.IntegerField()),
                ('card_holder', models.CharField(max_length=80)),
                ('cv2', models.IntegerField()),
                ('postal_code', models.IntegerField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Client')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField()),
                ('updated_date', models.DateTimeField()),
                ('deleted_date', models.DateTimeField(blank=True, db_index=True, null=True)),
                ('birth_date', models.DateField()),
                ('last_login_date', models.DateField()),
                ('bus_route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.BusRoute')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BusRouteTicket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField()),
                ('updated_date', models.DateTimeField()),
                ('deleted_date', models.DateTimeField(blank=True, db_index=True, null=True)),
                ('amount_payed', models.FloatField()),
                ('bus_route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.BusRoute')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Client')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='busroute',
            name='district',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.District'),
        ),
    ]
