# Generated by Django 3.2.3 on 2021-05-19 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_alter_order_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='mobile',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
    ]