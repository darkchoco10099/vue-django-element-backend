# Generated by Django 2.2.26 on 2022-05-05 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('center', '0002_auto_20220505_1643'),
    ]

    operations = [
        migrations.CreateModel(
            name='DemoApi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fwl', models.IntegerField()),
                ('yyyj', models.IntegerField()),
                ('yymb', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Project',
        ),
    ]