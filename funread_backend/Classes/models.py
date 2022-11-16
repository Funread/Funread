from django.db import models
from TeacherApp.models import Teachers

# Create your models here.
class Classes(models.Model):
    classesid = models.AutoField(primary_key=True)  
    name = models.CharField(max_length=200, blank=True, null=True) 
    grade = models.IntegerField(blank=True, null=True)
    teacherassigned = models.ForeignKey(Teachers, related_name='teacherassigned1',db_column='teacherassigned', on_delete=models.CASCADE, to_field='TeacherId')
    createdat = models.DateTimeField(blank=True, null=True)  
    lastupdateat = models.DateTimeField(blank=True, null=True)  
 