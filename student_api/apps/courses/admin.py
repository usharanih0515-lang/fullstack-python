from django.contrib import admin
from .models import Course, Enrollment

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['course_code', 'title', 'teacher', 'department', 'credits', 'status']
    list_filter = ['status', 'department', 'credits']
    search_fields = ['course_code', 'title']

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ['student', 'course', 'enrollment_date', 'status']
    list_filter = ['status']
    search_fields = ['student__student_id', 'course__course_code']
