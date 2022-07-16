# Generated by Django 4.0.6 on 2022-07-16 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0003_reservation_client_delete_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='status',
            field=models.TextField(choices=[('Reserved', 'Зарезервирован'), ('Wait', 'Ожидает подтверждения')], default='Wait'),
        ),
    ]
