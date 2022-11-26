# Generated by Django 4.1.2 on 2022-11-26 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_userimage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='user',
            new_name='parent',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(default='user/default.png', upload_to='user/image'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('m', 'Male'), ('f', 'Female'), ('o', 'Other')], default='o', max_length=3),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='name',
            field=models.CharField(default='<anon>', max_length=256),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='works_at',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]
