# Generated by Django 4.0.2 on 2022-04-22 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_widget_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='widget',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
