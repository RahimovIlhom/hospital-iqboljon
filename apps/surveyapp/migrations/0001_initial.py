# Generated by Django 5.1.5 on 2025-01-21 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PatientData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=255, verbose_name='Bemor FISH')),
                ('age', models.CharField(max_length=50, verbose_name='Yosh')),
                ('housing_or_working_conditions', models.CharField(max_length=255, verbose_name='Turar joy, ish sharoiti')),
                ('smoking', models.CharField(max_length=255, verbose_name='Chekish')),
                ('cold_exposure', models.CharField(max_length=4, verbose_name='Sovuq qotish')),
                ('contact_with_allergens', models.CharField(max_length=4, verbose_name='Allergenlar bilan kontakt')),
                ('hereditary_predisposition', models.CharField(max_length=4, verbose_name='Irsiy moyillik')),
                ('onset_of_disease', models.CharField(max_length=50, verbose_name='Kasallik boshlanishi')),
                ('course_of_disease', models.CharField(max_length=50, verbose_name='Kasallik kechishi')),
                ('attack_course', models.CharField(max_length=4, verbose_name='Xurujli kechishi')),
                ('treatment_effectiveness', models.CharField(max_length=50, verbose_name='Davo samaradorlik')),
                ('cough', models.CharField(max_length=4, verbose_name="Yo'tal")),
                ('cough_attack', models.CharField(max_length=50, verbose_name="Yo'tal xuruji")),
                ('phlegm', models.CharField(max_length=4, verbose_name="Balg'am")),
                ('what_sputum', models.CharField(max_length=50, verbose_name="Qanday balg'am")),
                ('shortness_of_breath', models.CharField(max_length=4, verbose_name='Xansirash')),
                ('what_suffocation', models.CharField(max_length=50, verbose_name='Qanday xansirash')),
                ('pain', models.CharField(max_length=4, verbose_name="Og'riq")),
                ('temperature', models.CharField(max_length=4, verbose_name='Harorat')),
                ('what_temperature', models.CharField(max_length=50, verbose_name='Qanday harorat')),
                ('breath_sound_types', models.JSONField(verbose_name='Nafas shovqini turi')),
                ('breath_sound_location', models.JSONField(verbose_name='Lokalizatsiya')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Bemor',
                'verbose_name_plural': 'Bemorlar',
                'ordering': ['-created_at'],
            },
        ),
    ]
