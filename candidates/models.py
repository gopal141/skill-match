from django.db import models
from django.utils.safestring import mark_safe
from django.core.validators import RegexValidator

# Create your models here.
Status_choice = [
    ('active', 'active'),
    ('inactive', 'inactive')
]

job_status = [
    ('Under Review', 'Under Review'),
    ('Shown Interest', 'Shown Interest'),
    ('Rejected', 'Rejected')
]

class login_table(models.Model):
    email_id = models.EmailField(max_length=50)
    phone_no = models.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                regex='^[0-9]{10}$',
                message= 'please enter valid number',
                code='INVALID_NUMBER'
            )
        ]
    )
    dp = models.ImageField(upload_to='photos/dp')
    password = models.CharField(max_length=50)
    Role = models.CharField(max_length=50)
    Status = models.CharField(max_length=50, choices=Status_choice)

    def admin_photo(self):
        return mark_safe('<img src="{}" width="200px"/>'.format(self.dp.url))

class state_table(models.Model):
    state_name = models.CharField(max_length=50)


class city(models.Model):
    city_name = models.CharField(max_length=50)
    state_id = models.ForeignKey(state_table, on_delete=models.CASCADE)

class area_table(models.Model):
    city_id = models.ForeignKey(city, on_delete=models.CASCADE)
    state_id = models.ForeignKey(state_table,on_delete=models.CASCADE)
    area_name = models.CharField(max_length=50)

class university_table(models.Model):
    university_name = models.CharField(max_length=50)

class college_table(models.Model):
    college_name = models.CharField(max_length=50)
    university_id = models.ForeignKey(university_table, on_delete=models.CASCADE)

class branch_table(models.Model):
    college_id = models.ForeignKey(college_table, on_delete=models.CASCADE)
    university_id = models.ForeignKey(university_table, on_delete=models.CASCADE)
    branch_name = models.CharField(max_length=50)

class user_detail_table(models.Model):
    l_id = models.ForeignKey(login_table,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    dob = models.DateField()
    address = models.CharField(max_length=200)
    area_id = models.ForeignKey(area_table,on_delete=models.CASCADE)
    city_id = models.ForeignKey(city, on_delete=models.CASCADE)
    state_id = models.ForeignKey(state_table, on_delete=models.CASCADE)
    branch_id = models.ForeignKey(branch_table, on_delete=models.CASCADE)
    college_id = models.ForeignKey(college_table, on_delete=models.CASCADE)
    university_id = models.ForeignKey(university_table, on_delete=models.CASCADE)

class company_details(models.Model):
    l_id = models.ForeignKey(login_table, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=50)
    company_type = models.CharField(max_length=50)
    company_address = models.CharField(max_length=200)
    company_website = models.CharField(max_length=200)
    founded_year = models.DateField()
    company_support_mail = models.EmailField(max_length=50)
    company_support_phone = models.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                regex='^[0-9]{10}$',
                message= 'please enter valid number',
                code='INVALID_NUMBER'
            )
        ]
    )
    company_size = models.CharField(max_length=50)
    company_city = models.CharField(max_length=50)
    company_area = models.CharField(max_length=200)

class skills_table(models.Model):
    skills_name = models.CharField(max_length=50)

class requirement_jobs(models.Model):
    company_id = models.ForeignKey(company_details, on_delete=models.CASCADE)
    job_type = models.CharField(max_length=50)
    job_description = models.TextField()
    vacancy = models.IntegerField()
    basic_pay = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()

class user_skill_table(models.Model):
    l_id = models.ForeignKey(login_table, on_delete=models.CASCADE)
    skills_id = models.ForeignKey(skills_table, on_delete=models.CASCADE)
    skill_level = models.IntegerField()

class resume_table(models.Model):
    l_id = models.ForeignKey(login_table, on_delete=models.CASCADE)
    file_path = models.FileField(upload_to='doc')

    def admin_doc(self):
        return mark_safe('<doc src="{}" width="100"/>'.format(self.doc.url))

    admin_doc.allow_tags = True

class feedback(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    comment = models.TextField()

class appliedjob(models.Model):
    l_id = models.ForeignKey(login_table, on_delete=models.CASCADE)
    applied_job_id = models.ForeignKey(requirement_jobs, on_delete=models.CASCADE)
    candidate_details = models.ForeignKey(user_detail_table, on_delete=models.CASCADE)
    applied_company_id = models.ForeignKey(company_details, on_delete=models.CASCADE)
    applied_datetime = models.DateTimeField(auto_now_add=True)
    candidate_resume = models.ForeignKey(resume_table, on_delete=models.CASCADE)
    applied_job_status = models.CharField(max_length=50, choices=job_status)
    show_interest_button = models.BooleanField()
    rejected = models.BooleanField()