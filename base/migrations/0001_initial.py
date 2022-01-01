# Generated by Django 3.2.7 on 2022-01-01 01:58

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=30)),
                ('last_name', models.CharField(blank=True, max_length=30)),
                ('username', models.CharField(blank=True, max_length=30)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('location', django_countries.fields.CountryField(blank=True, max_length=2)),
                ('talent', models.TextField(blank=True, max_length=50)),
                ('password', models.CharField(blank=True, max_length=30)),
                ('password_confirmation', models.CharField(blank=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Freelancer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=30)),
                ('last_name', models.CharField(blank=True, max_length=30)),
                ('username', models.CharField(blank=True, max_length=30)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('location', django_countries.fields.CountryField(blank=True, default='Ethiopia', max_length=2)),
                ('bio', models.TextField(blank=True, max_length=40)),
                ('talent', models.TextField(blank=True, max_length=50)),
                ('password', models.CharField(blank=True, max_length=30)),
                ('password_confirmation', models.CharField(blank=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(blank=True, max_length=30)),
                ('salary', models.CharField(blank=True, max_length=30)),
                ('deadline', models.DateTimeField()),
                ('job_description', models.TextField(blank=True, max_length=500)),
                ('restrictions', models.CharField(blank=True, max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.employer')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lebel', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proposal', models.TextField(blank=True, max_length=500)),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.employer')),
                ('freelancer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.freelancer')),
                ('job_title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.job')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(blank=True, max_length=500)),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.employer')),
                ('freelancer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.freelancer')),
            ],
        ),
        migrations.AddField(
            model_name='job',
            name='level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.level'),
        ),
        migrations.AddField(
            model_name='freelancer',
            name='level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.level'),
        ),
    ]
