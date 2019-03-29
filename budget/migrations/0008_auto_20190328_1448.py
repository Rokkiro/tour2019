# Generated by Django 2.1.7 on 2019-03-28 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0007_auto_20190319_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='rate',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='money',
            name='amount_cur',
            field=models.FloatField(blank=True, default=0.0),
        ),
    ]
