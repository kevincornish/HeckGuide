# Generated by Django 3.2.5 on 2021-09-16 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worldsegments',
            name='object_id',
            field=models.BigIntegerField(db_index=True, null=True),
        ),
    ]
