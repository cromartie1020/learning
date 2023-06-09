# Generated by Django 4.2 on 2023-05-06 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('entry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logs.topic')),
            ],
        ),
    ]
