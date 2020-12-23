# Generated by Django 3.1.4 on 2020-12-23 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mplan', '0002_auto_20201212_2234'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='amount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='name',
            field=models.CharField(blank=True, max_length=512),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='food_id',
            field=models.IntegerField(),
        ),
    ]
