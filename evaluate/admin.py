from users.admin import ProfileAdmin
from django.contrib import admin
from evaluate import models
# Register your models here.

class TestsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'test_name', 'no_of_ans', 'total_marks', 'passing_marks', 'uploaded_at')
    list_display_links = ('id', 'user', 'test_name', 'no_of_ans', 'total_marks', 'passing_marks', 'uploaded_at')
    search_fields = ('id', 'test_name')
    list_per_page = 20

admin.site.register(models.Test, TestsAdmin)
