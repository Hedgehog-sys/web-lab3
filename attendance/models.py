from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """Кастомная модель пользователя СТИ НИЯУ МИФИ"""
    
    @property
    def is_student(self):
        # Проверяем, существует ли у юзера связанный профиль студента
        return hasattr(self, 'student_profile')

    @property
    def is_teacher(self):
        # Проверяем, существует ли у юзера связанный профиль преподавателя
        return hasattr(self, 'teacher_profile')


class Student(models.Model):
    """Профиль студента"""
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE, 
        related_name='student_profile',
        verbose_name="Пользователь"
    )
    group = models.CharField(max_length=20, verbose_name="Группа")

    def __str__(self):
        return f"Студент: {self.user.username} ({self.group})"


class Teacher(models.Model):
    """Профиль преподавателя"""
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE, 
        related_name='teacher_profile',
        verbose_name="Пользователь"
    )
    department = models.CharField(max_length=100, verbose_name="Кафедра", default="ЭAFU")

    def __str__(self):
        return f"Преподаватель: {self.user.username}"
