from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """Кастомный пользователь (слайд 3 лекции 3)"""
    @property
    def is_student(self):
        return hasattr(self, 'student')

    @property
    def is_teacher(self):
        return hasattr(self, 'teacher')

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    group = models.CharField(max_length=20)

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100, default="ЭAFU")
