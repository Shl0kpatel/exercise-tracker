# Generated by Django 5.1.7 on 2025-03-13 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0002_alter_customuser_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='reps',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='sets',
            field=models.IntegerField(default=1),
        ),
    ]
