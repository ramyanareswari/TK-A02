# Generated by Django 4.1.2 on 2022-10-29 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Send_FoodWaste_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone_number', models.IntegerField()),
                ('address', models.TextField()),
                ('food_type', models.CharField(max_length=50)),
                ('expiry_date', models.DateField()),
                ('weight', models.IntegerField()),
            ],
        ),
    ]
