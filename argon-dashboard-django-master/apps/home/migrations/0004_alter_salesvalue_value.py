# Generated by Django 3.2.6 on 2023-12-28 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_totalorders'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesvalue',
            name='value',
            field=models.IntegerField(),
        ),
    ]