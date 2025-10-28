# colleges/admin.py
from django.contrib import admin
from .models import City, Course, College

@admin.register(College)
class CollegeAdmin(admin.ModelAdmin):
    # --- ADD 'rank_source' TO THIS LIST ---
    list_display = ('name', 'city', 'rank', 'rank_source', 'college_type')
    
    list_filter = ('city', 'college_type')
    search_fields = ('name', 'city__name')
    filter_horizontal = ('courses',) 

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'duration_in_years', 'average_fees')

admin.site.register(City)