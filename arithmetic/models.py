from django.db import models

# Create your models here.
class Rule(models.Model):
    rule_text=models.CharField(max_length=100)
    rule_image=models.ImageField(blank=True)

class Student(models.Model):
    #Student_Age=models.IntegerField()
    student_name=models.CharField(max_length=50)
    #Lasr_Name=models.CharField(max_length=50)
    #Schedule=models.
    #Scores =
    rules_set = models.ManyToManyField(Rule)
