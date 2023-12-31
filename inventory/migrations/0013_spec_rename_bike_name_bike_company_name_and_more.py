# Generated by Django 4.1.1 on 2023-08-17 04:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0012_details_bike'),
    ]

    operations = [
        migrations.CreateModel(
            name='Spec',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=50)),
                ('top_speed', models.IntegerField()),
                ('fuel', models.CharField(max_length=50)),
                ('engine_cc', models.IntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name='bike',
            old_name='bike_name',
            new_name='company_name',
        ),
        migrations.AlterField(
            model_name='bike',
            name='details',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.spec'),
        ),
        migrations.DeleteModel(
            name='Details',
        ),
    ]
