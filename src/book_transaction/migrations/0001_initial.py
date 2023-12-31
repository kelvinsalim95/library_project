# Generated by Django 4.2.5 on 2023-09-09 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BorrowedBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('book', models.CharField(max_length=100)),
                ('user_mapper', models.CharField(max_length=100)),
                ('borrowed_date', models.DateTimeField(auto_now_add=True)),
                ('return_date', models.DateTimeField()),
                ('renewed', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
