# Generated by Django 2.1.7 on 2019-03-08 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0005_auto_20190308_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='money',
            name='comment',
            field=models.CharField(blank=True, default='', max_length=300),
        ),
    ]