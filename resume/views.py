from django.shortcuts import render
from .models import *

# Create your views here.

def tnc(request):
    return render(request,'tnc.html')

def about(request):
    return render(request,'about.html')

def home(request):
    return render(request,'home.html')

def main(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        contact=request.POST.get('contact')
        email=request.POST.get('email')
        address=request.POST.get('address')
        image=request.FILES.get('image')
        print(image,name)
        linkedln=request.POST.get('linkedln')
        github=request.POST.get('github')
        insta=request.POST.get('insta')
        skill1=request.POST.get('skill1')
        skill2=request.POST.get('skill2')
        skill3=request.POST.get('skill3')
        skill4=request.POST.get('skill4')
        objective=request.POST.get('objective')
        work1=request.POST.get('work1')
        work2=request.POST.get('work2')
        edu1=request.POST.get('edu1')
        edu2=request.POST.get('edu2')
        ih1=request.POST.get('ih1')
        ih2=request.POST.get('ih2')
        ref=request.POST.get('ref')
        print(image)

        resume=Resume(name=name,
        contact=contact,
        email=email,
        address=address,
        image=image,
        linkedln=linkedln,
        github=github,
        insta=insta,
        skill1=skill1,
        skill2=skill2,
        skill3=skill3,
        skill4=skill4,
        objective=objective,
        work1=work1,
        work2=work2,
        edu1=edu1,
        edu2=edu2,
        ih1=ih1,
        ih2=ih2,
        ref=ref
        )
        resume.save()
        return render(request,'carousal.html')

    return render(request,'main.html')

def policy(request):
    return render(request,'policy.html')

def generatecv(request):
    return render(request,'carousal.html')

def format1(request):
    data = Resume.objects.latest('created_on')
    context = {
            'data':data,
        }
    return render(request,'format1.html',context)

def format2(request):
    data = Resume.objects.latest('created_on')
    context = {
            'data':data,
        }
    return render(request,'format2.html',context)

def format3(request):
    data = Resume.objects.latest('created_on')
    context = {
            'data':data,
        }
    return render(request,'format3.html',context)

def format4(request):
    data = Resume.objects.latest('created_on')
    context = {
            'data':data,
        }
    return render(request,'format4.html',context)