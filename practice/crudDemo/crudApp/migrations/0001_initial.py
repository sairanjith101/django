# Generated by Django 4.2.5 on 2023-09-19 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sno', models.IntegerField()),
                ('Sname', models.CharField(max_length=30)),
                ('Sclass', models.IntegerField()),
                ('Saddress', models.CharField(max_length=50)),
            ],
        ),
    ]
