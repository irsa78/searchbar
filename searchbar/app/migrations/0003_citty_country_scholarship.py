# Generated by Django 3.0.5 on 2020-04-25 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_author_category_journal'),
    ]

    operations = [
        migrations.CreateModel(
            name='Citty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Scholarship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=255)),
                ('research', models.CharField(max_length=255)),
                ('city', models.ManyToManyField(to='app.Citty')),
                ('country', models.ManyToManyField(to='app.Country')),
            ],
            options={
                'verbose_name_plural': 'scholarships',
            },
        ),
    ]
