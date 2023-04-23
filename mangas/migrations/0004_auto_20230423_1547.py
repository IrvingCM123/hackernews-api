# Generated by Django 3.1.3 on 2023-04-23 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mangas', '0003_auto_20230423_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manga',
            name='capitulosmanga',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='manga',
            name='clasificacionedadmanga',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='manga',
            name='descripcionmanga',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='manga',
            name='editorialmanga',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='manga',
            name='escritormanga',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='manga',
            name='generomanga',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='manga',
            name='ilustradormanga',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='manga',
            name='titulomanga',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='manga',
            name='volumenesmanga',
            field=models.IntegerField(default=0),
        ),
    ]
