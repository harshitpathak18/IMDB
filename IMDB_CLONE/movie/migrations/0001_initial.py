# Generated by Django 3.2.10 on 2022-07-17 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField(max_length=1000)),
                ('genre', models.CharField(choices=[('C', 'COMEDY'), ('D', 'DRAMA'), ('S', 'SCI-FI'), ('A', 'ACTION')], max_length=1)),
                ('rating', models.DecimalField(decimal_places=2, max_digits=3)),
                ('trailer_link', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='images')),
                ('poster', models.ImageField(upload_to='poster')),
            ],
        ),
    ]