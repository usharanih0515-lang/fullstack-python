from django.contrib import admin
from .models import Department, StudentProfile, TeacherProfile

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'head_of_department']
    search_fields = ['name']

@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ['student_id', 'user', 'department', 'year_level', 'status']
    list_filter = ['year_level', 'status', 'department']
    search_fields = ['student_id', 'user__username', 'user__first_name', 'user__last_name']

@admin.register(TeacherProfile)
class TeacherProfileAdmin(admin.ModelAdmin):
    list_display = ['employee_id', 'user', 'department', 'employment_type']
    list_filter = ['employment_type', 'department']
    search_fields = ['employee_id', 'user__username', 'user__first_name', 'user__last_name']
