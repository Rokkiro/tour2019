# Generated by Django 2.1.7 on 2019-03-29 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0011_auto_20190329_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='money',
            name='sign',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='budget.Sign', verbose_name='Приход\\Расход'),
        ),
    ]
