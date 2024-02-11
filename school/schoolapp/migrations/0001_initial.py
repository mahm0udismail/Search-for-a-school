# Generated by Django 5.0.1 on 2024-02-03 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='school',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.TextField()),
                ('school_code', models.TextField()),
                ('school_type', models.CharField(choices=[('National', 'National'), ('International', 'International'), ('public', 'public')], max_length=50)),
                ('school_grade', models.CharField(choices=[('KG1', 'KG1'), ('KG2', 'KG2'), ('1primary', '1primary'), ('2primary', '2primary'), ('3primary', '3primary'), ('4primary', '4primary'), ('5primary', '5primary'), ('6primary', '6primary'), ('1secondary', '1secondary'), ('2secondary', '2secondary'), ('3secondary', '3secondary')], max_length=50)),
            ],
        ),
    ]