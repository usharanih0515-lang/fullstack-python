from django.contrib import admin
from .models import Grade

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ['student', 'course', 'score', 'letter_grade', 'teacher', 'graded_at']
    list_filter = ['letter_grade', 'course']
    search_fields = ['student__student_id', 'course__course_code']
    readonly_fields = ['letter_grade']
