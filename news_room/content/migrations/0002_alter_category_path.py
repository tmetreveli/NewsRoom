# Generated by Django 5.0.2 on 2024-02-11 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='path',
            field=models.CharField(default='', max_length=100),
        ),
    ]
