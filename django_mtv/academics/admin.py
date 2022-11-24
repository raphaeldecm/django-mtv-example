from django.contrib import admin

from .models import Subject, Course, Clazz


class SubjectAdmin(admin.ModelAdmin):
    search_fields = ["name"]


class CourseAdmin(admin.ModelAdmin):
    search_fields = ["name"]


class ClazzAdmin(admin.ModelAdmin):
    search_fields = ["name"]


admin.site.register(Subject, SubjectAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Clazz, ClazzAdmin)
