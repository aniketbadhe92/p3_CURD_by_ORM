# Generated by Django 4.2.4 on 2023-09-10 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ename', models.CharField(max_length=30)),
                ('salary', models.IntegerField()),
                ('city', models.CharField(max_length=30)),
            ],
        ),
    ]
