# Generated by Django 4.2.5 on 2023-09-09 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='type',
            field=models.CharField(choices=[('student', 'Student'), ('librarian', 'Librarian')], max_length=255),
        ),
    ]