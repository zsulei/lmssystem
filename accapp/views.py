from django.shortcuts import render
from .forms import ClientCreationForm
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        student_form = ClientCreationForm(request.POST)
        if student_form.is_valid():
            new_student = student_form.save(commit=False)
            new_student.set_password(student_form.cleaned_data['password'])
            new_student.save()
            messages.success(request, 'Registration is done!!!')
            return render(request, 'registration/login.html', {'new_student': new_student})
    else:
        student_form = ClientCreationForm()
    return render(request, 'registration/registration.html', {'student_form': student_form})
