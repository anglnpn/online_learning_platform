# Generated by Django 5.0.2 on 2024-02-20 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0004_alter_lesson_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name': 'курс', 'verbose_name_plural': 'курсы'},
        ),
        migrations.AlterModelOptions(
            name='lesson',
            options={'verbose_name': 'урок', 'verbose_name_plural': 'уроки'},
        ),
    ]