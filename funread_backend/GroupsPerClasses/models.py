from django.db import models
from Users.models import User
from Books.models import Book

# Create your models here.

class GroupsPerClasses(models.Model):
    groupsPerClassesId = models.AutoField(primary_key=True)
    groupsId = models.ForeignKey(Book, related_name='groupsId',db_column='groupsId', on_delete=models.CASCADE, to_field='groupsId')
    classesId = models.ForeignKey(User, related_name='classesId',db_column='classesId', on_delete=models.CASCADE, to_field='classesId')
