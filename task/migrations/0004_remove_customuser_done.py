# Generated by Django 4.2.2 on 2023-07-02 22:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_customuser_done'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='done',
        ),
    ]