# Generated by Django 4.0 on 2021-12-26 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Table_booked',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('no_of_persons', models.IntegerField()),
                ('message', models.TextField()),
            ],
        ),
    ]
