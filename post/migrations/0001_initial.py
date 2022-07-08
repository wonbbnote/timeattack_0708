# Generated by Django 4.0.4 on 2022-06-17 06:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=128)),
            ],
            options={
                'db_table': 'business_areas',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=128)),
            ],
            options={
                'db_table': 'companies',
            },
        ),
        migrations.CreateModel(
            name='JobPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('company_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='post.company')),
            ],
            options={
                'db_table': 'job_posts',
            },
        ),
        migrations.CreateModel(
            name='JobType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_type', models.CharField(max_length=128)),
            ],
            options={
                'db_table': 'job_types',
            },
        ),
        migrations.CreateModel(
            name='SkillSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
            options={
                'db_table': 'skill_sets',
            },
        ),
        migrations.CreateModel(
            name='JobPostSkillSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='post.jobpost')),
                ('skill_set', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='post.skillset')),
            ],
        ),
        migrations.AddField(
            model_name='jobpost',
            name='job_type_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='post.jobtype'),
        ),
        migrations.CreateModel(
            name='CompanyBusinessArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_area', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='post.businessarea')),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='post.company')),
            ],
            options={
                'db_table': 'company_business_areas',
            },
        ),
        migrations.AddField(
            model_name='company',
            name='business_area',
            field=models.ManyToManyField(through='post.CompanyBusinessArea', to='post.businessarea'),
        ),
    ]
