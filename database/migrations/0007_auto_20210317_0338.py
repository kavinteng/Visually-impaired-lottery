# Generated by Django 3.1.7 on 2021-03-16 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0006_auto_20210317_0329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lottery',
            name='num',
            field=models.CharField(max_length=6),
        ),
    ]