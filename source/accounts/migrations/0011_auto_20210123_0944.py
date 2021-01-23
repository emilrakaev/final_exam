# Generated by Django 2.2 on 2021-01-23 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20210121_2319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authtoken',
            name='type',
            field=models.CharField(choices=[('password_reset', 'Восстановление пароля'), ('register', 'Регистрация')], default='register', max_length=20, verbose_name='Тип токена'),
        ),
    ]