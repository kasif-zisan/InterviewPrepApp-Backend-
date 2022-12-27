# Generated by Django 4.1.4 on 2022-12-27 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postLink', models.URLField()),
                ('type', models.CharField(choices=[('hate', 'hate'), ('spam', 'spam'), ('irrelevant', 'irrelevant')], default='spam', max_length=20)),
            ],
        ),
    ]
