# Generated by Django 5.0.4 on 2024-04-05 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grouppaper',
            name='papers',
            field=models.ManyToManyField(blank=True, to='papers.paper'),
        ),
        migrations.AlterField(
            model_name='recommendpaperslist',
            name='papers',
            field=models.ManyToManyField(blank=True, to='papers.paper'),
        ),
    ]
