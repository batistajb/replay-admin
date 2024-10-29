# Generated by Django 5.1.1 on 2024-10-29 20:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('cnpj', models.CharField(max_length=18, null=True, unique=True)),
                ('address', models.TextField()),
                ('phone', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('cnpj', models.CharField(max_length=18, null=True, unique=True)),
                ('address', models.TextField()),
                ('phone', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='PlanPartner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('partner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plans', to='core.partner')),
            ],
        ),
        migrations.CreateModel(
            name='Quatrain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('type', models.CharField(choices=[('soccer', 'Soccer'), ('volleyball', 'Volleyball'), ('basketball', 'Basketball'), ('tennis', 'Tennis'), ('handball', 'Handball'), ('futsal', 'Futsal'), ('beach_tennis', 'Beach Tennis')], default='soccer', max_length=50)),
                ('availability', models.BooleanField(default=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quatrains', to='core.client')),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days', models.IntegerField(help_text='Número de dias de exibição')),
                ('partner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medias', to='core.partner')),
                ('quatrain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medias', to='core.quatrain')),
            ],
        ),
    ]
