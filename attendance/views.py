# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

@login_required
def profile_redirect_view(request):
    """Вьюха-диспетчер: перенаправляет пользователя после логина по его роли"""
    user = request.user

    if user.is_teacher:
        return redirect('teacher_dashboard')
    elif user.is_student:
        return redirect('student_dashboard')
    else:
        return redirect('common_dashboard')

@login_required
def student_dashboard(request):
    """Кабинет студента (Задание 3)"""
    if not request.user.is_student:
        return HttpResponseForbidden("Ошибка 403: Доступ запрещен. Вы не являетесь студентом.")
    return render(request, 'attendance/student_dashboard.html')

@login_required
def teacher_dashboard(request):
    """Кабинет преподавателя (Задание 3)"""
    if not request.user.is_teacher:
        return HttpResponseForbidden("Ошибка 403: Доступ запрещен. Вы не являетесь преподавателем.")
    return render(request, 'attendance/teacher_dashboard.html')

@login_required
def common_dashboard(request):
    """Общая страница для пользователей без профиля"""
    return render(request, 'attendance/common_dashboard.html')
