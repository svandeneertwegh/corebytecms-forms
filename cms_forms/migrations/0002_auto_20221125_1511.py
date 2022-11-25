# Generated by Django 3.2 on 2022-11-25 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_forms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formsubmission',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='formsubmission',
            name='language',
            field=models.CharField(choices=[('en', 'English')], default='en', max_length=10, verbose_name='form language'),
        ),
        migrations.AlterField(
            model_name='option',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
