# Generated by Django 4.2.5 on 2023-09-19 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='amount',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]