# Generated by Django 3.2.25 on 2024-04-19 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baza_v1', '0002_auto_20240419_1838'),
    ]

    operations = [
        migrations.RenameField(
            model_name='airport',
            old_name='eff_date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='airport',
            old_name='loc_id',
            new_name='location_id',
        ),
        migrations.RenameField(
            model_name='airport',
            old_name='site_num',
            new_name='site_number',
        ),
        migrations.RenameField(
            model_name='airport',
            old_name='fac_type',
            new_name='type',
        ),
        migrations.AddField(
            model_name='airport',
            name='commercial_aircraft_count',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='airport',
            name='flight_count',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='airport',
            name='helicopter_count',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='airport',
            name='jet_count',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='airport',
            name='military_aircraft_count',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='airport',
            name='region_code',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]