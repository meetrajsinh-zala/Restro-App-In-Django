# Generated by Django 5.0.3 on 2024-03-30 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=250)),
                ('Password', models.CharField(max_length=16)),
            ],
        ),
    ]