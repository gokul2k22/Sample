# Generated by Django 4.2.3 on 2023-08-05 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0009_addcart'),
    ]

    operations = [
        migrations.AddField(
            model_name='addcart',
            name='deleted',
            field=models.BooleanField(default=False, null=True),
        ),
    ]