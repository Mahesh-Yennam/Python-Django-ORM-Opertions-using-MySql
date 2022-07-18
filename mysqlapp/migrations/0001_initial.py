# Generated by Django 4.0.1 on 2022-07-18 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('contact', models.IntegerField(default=0)),
                ('password', models.CharField(max_length=15)),
                ('description', models.TextField(max_length=200)),
            ],
            options={
                'db_table': 'emp',
            },
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary', models.IntegerField()),
                ('month', models.CharField(max_length=20)),
                ('description', models.TextField(max_length=200)),
                ('emp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysqlapp.emp')),
            ],
            options={
                'db_table': 'account',
            },
        ),
    ]
