# Generated by Django 3.0.4 on 2020-06-02 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EMployee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=45)),
                ('lastName', models.CharField(max_length=45)),
                ('salary', models.FloatField()),
                ('email', models.CharField(max_length=45)),
                ('pic', models.CharField(max_length=45)),
            ],
        ),
    ]