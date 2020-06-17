# Generated by Django 3.0.7 on 2020-06-17 03:08

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
                ('province', models.CharField(choices=[('1', 'San Jose'), ('2', 'Alajuela'), ('3', 'Cartago'), ('4', 'Heredia'), ('5', 'Guanacaste'), ('6', 'Puntarenas'), ('7', 'Limon')], max_length=2)),
                ('district', models.CharField(choices=[('1', 'Carmen'), ('2', 'Merced'), ('3', 'Hospital'), ('4', 'San Antonio'), ('5', 'Sabanilla'), ('6', 'Palmares'), ('7', 'San Nicolás'), ('8', 'Tierra Blanca'), ('9', 'Orosi'), ('10', 'Mercedes'), ('11', 'Barva'), ('12', 'San Domingo'), ('13', 'Liberia'), ('14', 'Nicoya'), ('15', 'Sámara'), ('16', 'Paquera'), ('17', 'Cóbano'), ('18', 'Guacimal'), ('19', 'Guápiles'), ('20', 'Siquirres'), ('21', 'La Rita')], max_length=2)),
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
                ('balance', models.FloatField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
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
            name='driver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Driver'),
        ),
    ]