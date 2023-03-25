from django.contrib import admin
from .models import login_table,state_table,city,area_table,university_table,college_table,branch_table,user_detail_table,company_details,skills_table,requirement_jobs,user_skill_table,resume_table,feedback,appliedjob

# Register your models here.
class showlogintable(admin.ModelAdmin):
    list_display = ['email_id', 'phone_no', 'dp', 'password', 'Role', 'Status']
admin.site.register(login_table, showlogintable)

class showstatetable(admin.ModelAdmin):
    list_display = ['state_name']
admin.site.register(state_table, showstatetable)

class showcity(admin.ModelAdmin):
    list_display = ['city_name', 'state_id']
admin.site.register(city, showcity)

class showareatable(admin.ModelAdmin):
    list_display = ['city_id', 'state_id', 'area_name']
admin.site.register(area_table, showareatable)

class showuniversitytable(admin.ModelAdmin):
    list_display = ['university_name']
admin.site.register(university_table, showuniversitytable)

class showcollegetable(admin.ModelAdmin):
    list_display = ['college_name', 'university_id']
admin.site.register(college_table, showcollegetable)

class showbranchtable(admin.ModelAdmin):
    list_display = ['college_id', 'university_id', 'branch_name']
admin.site.register(branch_table, showbranchtable)

class showuserdetailtable(admin.ModelAdmin):
    list_display = ['l_id', 'name', 'dob', 'address', 'area_id', 'city_id', 'state_id', 'branch_id', 'college_id', 'university_id']
admin.site.register(user_detail_table, showuserdetailtable)

class showcompanydetails(admin.ModelAdmin):
    list_display = ['l_id', 'company_name', 'company_type', 'company_address', 'company_website', 'founded_year', 'company_support_mail', 'company_support_phone', 'company_size', 'company_city', 'company_area']
admin.site.register(company_details, showcompanydetails)

class showskilltable(admin.ModelAdmin):
    list_display = ['skills_name']
admin.site.register(skills_table, showskilltable)

class showrequirementjobs(admin.ModelAdmin):
    list_display = ['company_id', 'job_type', 'job_description', 'vacancy', 'basic_pay', 'date', 'time']
admin.site.register(requirement_jobs, showrequirementjobs)

class showuserskilltable(admin.ModelAdmin):
    list_display = ['l_id', 'skills_id', 'skill_level']
admin.site.register(user_skill_table, showuserskilltable)

class showresumetable(admin.ModelAdmin):
    list_display = ['l_id', 'file_path']
admin.site.register(resume_table, showresumetable)

class showfeedback(admin.ModelAdmin):
    list_display = ['name', 'email', 'comment']
admin.site.register(feedback, showfeedback)

class showappliedjob(admin.ModelAdmin):
    list_display = ['l_id', 'applied_job_id', 'candidate_details', 'applied_company_id', 'applied_datetime', 'candidate_resume', 'applied_job_status', 'show_interest_button', 'rejected']
admin.site.register(appliedjob, showappliedjob)