# Generated by Django 4.0.5 on 2022-07-04 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_postcount'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
    ]