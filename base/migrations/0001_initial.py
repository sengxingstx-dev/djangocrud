# Generated by Django 4.2.1 on 2023-05-22 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=6)),
                ('position', models.CharField(max_length=50)),
                ('salary', models.PositiveIntegerField()),
                ('address', models.TextField()),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('phone', models.CharField(max_length=30, unique=True)),
                ('birthday', models.DateField()),
                ('religion', models.CharField(choices=[('Buddhism', 'Buddhism'), ('Christianity', 'Christianity'), ('Islam', 'Islam'), ('etc', 'etc')], default='Buddhism', max_length=20)),
                ('addition_note', models.TextField(blank=True, null=True)),
            ],
        ),
    ]