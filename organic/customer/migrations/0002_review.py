# Generated by Django 3.2.12 on 2022-04-16 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('star', models.CharField(max_length=100)),
                ('review', models.CharField(max_length=1000)),
            ],
        ),
    ]
