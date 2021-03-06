# Generated by Django 3.2.7 on 2021-10-18 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userbase',
            options={'verbose_name': 'Accounts', 'verbose_name_plural': 'Accounts'},
        ),
        migrations.RemoveField(
            model_name='userbase',
            name='address_1',
        ),
        migrations.RemoveField(
            model_name='userbase',
            name='address_2',
        ),
        migrations.RemoveField(
            model_name='userbase',
            name='phone',
        ),
        migrations.AddField(
            model_name='userbase',
            name='address_line_1',
            field=models.CharField(blank=True, max_length=60),
        ),
        migrations.AddField(
            model_name='userbase',
            name='address_line_2',
            field=models.CharField(blank=True, max_length=60),
        ),
        migrations.AddField(
            model_name='userbase',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AddField(
            model_name='userbase',
            name='town_city',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='userbase',
            name='first_name',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='userbase',
            name='postcode',
            field=models.CharField(blank=True, max_length=12),
        ),
    ]
