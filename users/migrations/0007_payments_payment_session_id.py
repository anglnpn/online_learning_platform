# Generated by Django 5.0.2 on 2024-02-24 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_remove_payments_payment_lesson'),
    ]

    operations = [
        migrations.AddField(
            model_name='payments',
            name='payment_session_id',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='идентификатор сессии платежа'),
        ),
    ]