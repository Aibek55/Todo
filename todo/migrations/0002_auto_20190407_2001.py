# Generated by Django 2.2 on 2019-04-07 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='status',
            field=models.CharField(choices=[('Doing', 'нужно сделать'), ('Done', 'сделано'), ('canceled', 'отменено')], default='doing', max_length=20),
        ),
    ]
