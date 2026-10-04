from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

@login_required
def profile_redirect_view(request):
    user = request.user
    if user.is_student:
        return redirect('/attendance/student/')
    elif user.is_teacher:
        return redirect('/attendance/teacher/')
    else:
        return redirect('/attendance/common/')

@login_required
def student_dashboard(request):
    if not request.user.is_student:
        return HttpResponseForbidden("Доступ запрещен.")
    return render(request, 'attendance/student_dashboard.html')

@login_required
def teacher_dashboard(request):
    if not request.user.is_teacher:
        return HttpResponseForbidden("Доступ запрещен.")
    return render(request, 'attendance/teacher_dashboard.html')

@login_required
def common_dashboard(request):
    return render(request, 'attendance/common_dashboard.html')
