# Generated by Django 3.1.5 on 2021-03-28 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('pclass', models.IntegerField(max_length=50)),
                ('sex', models.BooleanField()),
                ('age', models.IntegerField()),
                ('sibsp', models.IntegerField()),
            ],
        ),
    ]