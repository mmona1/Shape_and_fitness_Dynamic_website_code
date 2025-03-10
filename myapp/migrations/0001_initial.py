# Generated by Django 4.1.1 on 2023-06-18 05:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tile1', models.CharField(max_length=200)),
                ('limit', models.IntegerField()),
                ('slug', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('job_title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='image')),
                ('content_type', models.CharField(choices=[('slider', 'Slider'), ('card', 'Card'), ('testimonial', 'Testimonial')], max_length=20)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.category')),
            ],
        ),
    ]
