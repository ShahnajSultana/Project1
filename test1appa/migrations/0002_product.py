# Generated by Django 3.1.3 on 2020-12-01 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test1appa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
            ],
        ),
    ]