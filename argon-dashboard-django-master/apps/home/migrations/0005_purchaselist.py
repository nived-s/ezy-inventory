# Generated by Django 3.2.6 on 2023-12-28 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_salesvalue_value'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=255)),
                ('date', models.CharField(max_length=255)),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
            ],
        ),
    ]
