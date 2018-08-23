# Generated by Django 2.0.7 on 2018-08-23 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='create_profile',
            fields=[
                ('user_name', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=120, primary_key=True, serialize=False, unique=True)),
                ('password', models.CharField(max_length=120)),
            ],
        ),
    ]
