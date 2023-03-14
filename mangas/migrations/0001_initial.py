# Generated by Django 3.1.3 on 2023-02-26 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulomanga', models.TextField(default=' ')),
                ('generomanga', models.TextField(default=' ')),
                ('descripcionmanga', models.TextField(default=' ')),
                ('lanzamientomanga', models.DateTimeField(default=0)),
                ('escritormanga', models.TextField(default=' ')),
                ('volumenesmanga', models.IntegerField(blank=True, default=0)),
                ('capitulosmanga', models.IntegerField(blank=True, default=0)),
                ('ilustradormanga', models.TextField(default=' ')),
                ('editorialmanga', models.TextField(blank=True, default=' ')),
                ('clasificacionedadmanga', models.IntegerField(blank=True, default=0)),
            ],
        ),
    ]
