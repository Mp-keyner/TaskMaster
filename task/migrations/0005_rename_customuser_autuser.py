# Generated by Django 4.2.2 on 2023-07-02 22:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('task', '0004_remove_customuser_done'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CustomUser',
            new_name='autUser',
        ),
    ]
