# Generated by Django 4.1.5 on 2023-01-28 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emploie',
            name='commune',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
