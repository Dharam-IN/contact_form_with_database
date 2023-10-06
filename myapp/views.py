from django.shortcuts import render, HttpResponse
from myapp.models import StudentForm
from django.contrib import messages

# Create your views here.
def homepage(request):
    return render(request, 'home.html')

def signupform(request):
    if request.method=='POST':
        if request.POST.get('first_name') and request.POST.get('last_name') and request.POST.get('email') and request.POST.get('mobile_no') and request.POST.get('street_address') and request.POST.get('state') and request.POST.get('city'):
            saverecord = StudentForm()
            saverecord.first_name=request.POST.get('first_name')
            saverecord.middle_name=request.POST.get('middle_name')
            saverecord.last_name=request.POST.get('last_name')
            saverecord.email=request.POST.get('email')
            saverecord.mobile_no=request.POST.get('mobile_no')
            saverecord.street_address=request.POST.get('street_address')
            saverecord.state=request.POST.get('state')
            saverecord.city=request.POST.get('city')
            saverecord.course=request.POST.get('course')
            saverecord.duration=request.POST.get('duration')
            saverecord.save()
            messages.success(request, 'Record Saved Successfully...!')
            print(saverecord.first_name,saverecord.last_name,saverecord.course,saverecord.duration)
            return render(request, 'home.html')
        else:
            # return HttpResponse('condition false')
            return render(request, 'form.html')

    return render(request, 'form.html')
