from django.db import models
from django.conf import settings
from taggit.managers import TaggableManager

# Create your models here.

class Subject(models.Model):
    def __str__(self):
        return self.subject_name

    subject_name = models.CharField(max_length=50)

class Year(models.Model):
    def __str__(self):
        return(str(self.year_number))

    year_number = models.IntegerField()

class Rule(models.Model):
    def __str__(self):
        return self.rule_name
    rule_name = models.CharField(max_length=50)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    tags = TaggableManager()

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

class QuestionWithSelection(models.Model):
    def __str__(self):
        return self.QWS_name
    QWS_name = models.CharField(max_length=50)
    QWS_text = models.CharField(max_length=150)
    QWS_subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    QWS_year = models.ForeignKey(Year, on_delete=models.CASCADE)


class Selection(models.Model):
    def __str__(self):
        return self.selection_text
    question = models.ForeignKey(QuestionWithSelection, on_delete = models.CASCADE)
    selection_text=models.CharField(max_length=150)
    selection_correct = models.BooleanField()
    #selection_image=models.ImageField(blank=True)
