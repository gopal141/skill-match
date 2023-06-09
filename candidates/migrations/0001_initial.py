# Generated by Django 4.1.6 on 2023-03-09 13:18

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='area_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='branch_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='city',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='college_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='company_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=50)),
                ('company_type', models.CharField(max_length=50)),
                ('company_address', models.CharField(max_length=200)),
                ('company_website', models.CharField(max_length=200)),
                ('founded_year', models.DateField()),
                ('company_support_mail', models.EmailField(max_length=50)),
                ('company_support_phone', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(code='INVALID_NUMBER', message='please enter valid number', regex='^[0-9]{10}$')])),
                ('company_size', models.CharField(max_length=50)),
                ('company_city', models.CharField(max_length=50)),
                ('company_area', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('comment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='login_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_id', models.EmailField(max_length=50)),
                ('phone_no', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(code='INVALID_NUMBER', message='please enter valid number', regex='^[0-9]{10}$')])),
                ('dp', models.ImageField(upload_to='photos')),
                ('password', models.CharField(max_length=50)),
                ('Role', models.CharField(max_length=50)),
                ('Status', models.CharField(choices=[('active', 'active'), ('inactive', 'inactive')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='skills_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skills_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='state_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='university_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('university_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='user_skill_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_level', models.IntegerField()),
                ('l_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidates.login_table')),
                ('skills_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidates.skills_table')),
            ],
        ),
        migrations.CreateModel(
            name='user_detail_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('address', models.CharField(max_length=200)),
                ('area_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidates.area_table')),
                ('branch_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidates.branch_table')),
                ('city_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidates.city')),
                ('college_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidates.college_table')),
                ('l_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidates.login_table')),
                ('state_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidates.state_table')),
                ('university_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidates.university_table')),
            ],
        ),
        migrations.CreateModel(
            name='resume_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_path', models.FileField(upload_to='doc')),
                ('l_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidates.login_table')),
            ],
        ),
        migrations.CreateModel(
            name='requirement_jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_type', models.CharField(max_length=50)),
                ('job_description', models.TextField()),
                ('vacancy', models.IntegerField()),
                ('basic_pay', models.IntegerField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidates.company_details')),
            ],
        ),
        migrations.AddField(
            model_name='company_details',
            name='l_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidates.login_table'),
        ),
        migrations.AddField(
            model_name='college_table',
            name='university_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidates.university_table'),
        ),
        migrations.AddField(
            model_name='city',
            name='state_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidates.state_table'),
        ),
        migrations.AddField(
            model_name='branch_table',
            name='college_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidates.college_table'),
        ),
        migrations.AddField(
            model_name='branch_table',
            name='university_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidates.university_table'),
        ),
        migrations.AddField(
            model_name='area_table',
            name='city_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidates.city'),
        ),
        migrations.AddField(
            model_name='area_table',
            name='state_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidates.state_table'),
        ),
        migrations.CreateModel(
            name='appliedjob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applied_datetime', models.DateTimeField(auto_now_add=True)),
                ('applied_job_status', models.CharField(choices=[('Under Review', 'Under Review'), ('Shown Interest', 'Shown Interest'), ('Rejected', 'Rejected')], max_length=50)),
                ('show_interest_button', models.BooleanField()),
                ('rejected', models.BooleanField()),
                ('applied_company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidates.company_details')),
                ('applied_job_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidates.requirement_jobs')),
                ('candidate_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidates.user_detail_table')),
                ('candidate_resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidates.resume_table')),
                ('l_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidates.login_table')),
            ],
        ),
    ]
