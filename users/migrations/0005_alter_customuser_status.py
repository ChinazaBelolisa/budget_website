# Generated by Django 4.1.1 on 2022-09-21 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_customuser_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='status',
            field=models.CharField(choices=[('subscriber', 'subcriber'), ('regular', 'regular'), ('moderator', 'moderator')], default='regular', max_length=100),
        ),
    ]
