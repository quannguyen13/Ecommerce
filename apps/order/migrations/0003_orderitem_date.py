# Generated by Django 3.2.6 on 2021-09-02 02:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_alter_orderitem_vendor_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
