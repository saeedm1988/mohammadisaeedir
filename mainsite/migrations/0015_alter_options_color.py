# Generated by Django 4.0.3 on 2022-04-09 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0014_options_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='options',
            name='color',
            field=models.CharField(blank=True, default=None, max_length=8),
        ),
    ]