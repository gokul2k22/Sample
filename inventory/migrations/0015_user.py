# Generated by Django 4.1.1 on 2023-08-23 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0014_students'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identity', models.IntegerField()),
                ('qualification', models.CharField(max_length=50)),
                ('experiance', models.IntegerField()),
            ],
        ),
    ]
