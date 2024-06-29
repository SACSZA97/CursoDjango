# Generated by Django 5.0.6 on 2024-06-26 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cursos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(verbose_name='Nombre')),
                ('curso', models.TextField(verbose_name='Curso')),
                ('email', models.EmailField(max_length=254, verbose_name='Correo')),
                ('turno', models.CharField(max_length=10, verbose_name='turno')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='creado')),
                ('updated', models.DateTimeField(auto_now_add=True, verbose_name='actualizado')),
                ('imagen', models.ImageField(null=True, upload_to='fotos', verbose_name='INE')),
            ],
            options={
                'verbose_name': 'Curso',
                'verbose_name_plural': 'Cursos',
                'ordering': ['created'],
            },
        ),
    ]
