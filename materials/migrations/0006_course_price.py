# Generated by Django 5.0.2 on 2024-02-23 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0005_alter_course_options_alter_lesson_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='price',
            field=models.IntegerField(blank=True, null=True, verbose_name='цена курса'),
        ),
    ]
