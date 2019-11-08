from django.contrib import admin
from .models import Block, Subject, Rule, Student

# Register your models here.
class BlockInLine(admin.TabularInline):
    model=Block
    extra=1

class RuleAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name', {'fields':['rule_name']}),
    ]
    inline = [BlockInLine]

class StudentAdmin(admin.ModelAdmin):
    filter_horizontal=('rules_set',)
    fieldsets=[
    ('Name',{'fields':['student_name']}),
    ('Vocabulary',{'fields':['rules_set']})
    ]

class SubjectAdmin(admin.ModelAdmin):
    fieldsets=[
    ('Name', {'fields':['subject_name']}),
    ]


admin.site.register(Rule, RuleAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Subject, SubjectAdmin)
