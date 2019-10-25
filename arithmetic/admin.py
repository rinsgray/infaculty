from django.contrib import admin
from .models import Rule, Student

# Register your models here.
class RuleAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name', {'fields':['rule_name']}),
        ('Text', {'fields':['rule_text']}),
        ('Image',{'fields':['rule_image']}),
    ]
'''
class RulesInline(admin.StackedInline):
    model = Rule
    extra = 1
'''
class StudentAdmin(admin.ModelAdmin):
    fieldsets=[
    ('Name',{'fields':['student_name']}),
    ('Vocabulary',{'fields':['rules_set']})
    ]


admin.site.register(Rule, RuleAdmin)
admin.site.register(Student, StudentAdmin)
