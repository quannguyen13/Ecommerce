# Generated by Django 3.2.7 on 2021-09-08 04:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0008_alter_order_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='place',
            new_name='city',
        ),
    ]
