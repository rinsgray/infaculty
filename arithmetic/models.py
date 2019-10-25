from django.db import models

# Create your models here.
class Rule(models.Model):
    def __str__(self):
        return self.rule_name
    rule_name=models.CharField(max_length=50)
    rule_text=models.TextField()
    rule_image=models.ImageField(blank=True)

class Student(models.Model):
    def __str__(self):
        return self.student_name
    #Student_Age=models.IntegerField()
    student_name=models.CharField(max_length=50)
    #Lasr_Name=models.CharField(max_length=50)
    #Schedule=models.
    #Scores =
    rules_set = models.ManyToManyField(Rule)
