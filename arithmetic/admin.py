from django.contrib import admin
from .models import Block, Subject, Rule, Student, QuestionWithSelection, Selection,Year

# Register your models here.
class BlockInline(admin.StackedInline):
    model=Block
    extra=1

class RuleAdmin(admin.ModelAdmin):
    fieldsets = [('Subject',{'fields':['subject']}),
        ('Year',{'fields':['year']}),
        ('Name', {'fields':['rule_name']}),
        ('Tags',{'fields':['tags']})
    ]
    inlines = [BlockInline]

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

class YearAdmin(admin.ModelAdmin):
    fieldsets=[
    ('Number', {'fields':['year_number']}),
    ]

class SelectionAdmin(admin.StackedInline):
    model = Selection
    extra = 1

class QWSAdmin(admin.ModelAdmin):
    fieldsets=[('Subject',{'fields':['QWS_subject']}),
    ('Year',{'fields':['QWS_year']}),
    ('Name', {'fields':['QWS_name']}),
    ('Text', {'fields':['QWS_text']})
    ]
    inlines = [SelectionAdmin]




admin.site.register(Year, YearAdmin)
admin.site.register(Rule, RuleAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(QuestionWithSelection, QWSAdmin)
