# Generated by Django 4.1.2 on 2022-10-21 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateField(),
        ),
    ]
