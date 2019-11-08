from django.db import models

# Create your models here.

class Subject(models.Model):
    def __str__(self):
        return self.subject_name
    subject_name = models.CharField(max_length=50)


class Rule(models.Model):
    def __str__(self):
        return self.subject_name
    rule_name = models.CharField(max_length=50)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

class Block(models.Model):
    def __str__(self):
        return self.block_text
    rule=models.ForeignKey(Rule, on_delete=models.CASCADE)
    block_text=models.TextField()
    block_image=models.ImageField(blank=True)

class Student(models.Model):
    def __str__(self):
        return self.student_name
    #Student_Age=models.IntegerField()
    student_name=models.CharField(max_length=50)
    #Lasr_Name=models.CharField(max_length=50)
    #Schedule=models.
    #Scores =
    rules_set = models.ManyToManyField(Rule)
