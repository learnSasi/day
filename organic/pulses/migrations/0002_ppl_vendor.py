# Generated by Django 3.2.12 on 2022-04-16 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pulses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ppl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.FileField(upload_to='')),
                ('mobile_no', models.FileField(upload_to='')),
                ('gender', models.FileField(upload_to='')),
                ('password', models.FileField(upload_to='')),
                ('re_password', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.FileField(upload_to='')),
                ('mobile_no', models.FileField(upload_to='')),
                ('product_name', models.FileField(upload_to='')),
                ('location', models.FileField(upload_to='')),
                ('password', models.FileField(upload_to='')),
                ('re_password', models.FileField(upload_to='')),
            ],
        ),
    ]