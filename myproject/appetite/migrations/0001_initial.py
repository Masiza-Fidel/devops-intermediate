# Generated by Django 5.0.1 on 2024-01-30 12:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shoe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('loafers', 'Loafers'), ('sneakers', 'Sneakers'), ('official', 'Official'), ('sandals', 'Sandals'), ('boots', 'Boots'), ('casual', 'Casual')], default='casual', max_length=20)),
                ('brand', models.CharField(max_length=100)),
                ('model_name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('release_date', models.DateField()),
                ('is_featured', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ShoeImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='shoe_images/')),
                ('shoe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appetite.shoe')),
            ],
        ),
        migrations.CreateModel(
            name='ShoeVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='shoe_videos/')),
                ('shoe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appetite.shoe')),
            ],
        ),
    ]
