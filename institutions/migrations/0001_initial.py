# Generated by Django 2.0.3 on 2018-04-04 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Institutes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('i_name', models.CharField(max_length=30)),
                ('i_campus', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'institutes',
            },
        ),
    ]
