# Generated by Django 3.2.7 on 2021-09-09 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Key',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key_name', models.CharField(blank=True, max_length=100, null=True)),
                ('key_description', models.CharField(blank=True, max_length=200, null=True)),
                ('key', models.CharField(blank=True, max_length=15, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
