# Generated by Django 5.1.1 on 2024-09-08 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training_site_app', '0003_alter_lesson_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
