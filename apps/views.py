from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from apps.models import Contact
from users.models import User


# @login_required(login_url='/users/sign-in')
def home(request):
    students = User.objects.all().count()
    return render(request, 'birinchi_bet.html', {'students': students})

@login_required(login_url='/users/sign-in')
def kirish(request):
    return render(request,'python-course/1-kirish.html')

@login_required(login_url='/users/sign-in')
def ornatish(request):
    return render(request, 'python-course/2-ornatish.html')

@login_required(login_url='/users/sign-in')
def izoh(request):
    return render(request, 'python-course/3-izoh.html')

@login_required(login_url='/users/sign-in')
def ozgaruvchi(request):
    return render(request, 'python-course/4-ozgaruvchi.html')

@login_required(login_url='/users/sign-in')
def malumot_turi(request):
    return render(request, 'python-course/5-malumot-turi.html')

@login_required(login_url='/users/sign-in')
def sonlar(request):
    return render(request, 'python-course/6-sonlar.html')

@login_required(login_url='/users/sign-in')
def satr(request):
    return render(request, 'python-course/7-satr.html')

@login_required(login_url='/users/sign-in')
def mantiq(request):
    return render(request, 'python-course/8-mantiq.html')

@login_required(login_url='/users/sign-in')
def operator(request):
    return render(request, 'python-course/9-operator.html')

@login_required(login_url='/users/sign-in')
def list_(request):
    return render(request, 'python-course/10-list.html')

@login_required(login_url='/users/sign-in')
def tuple_(request):
    return render(request, 'python-course/11-tuple.html')

@login_required(login_url='/users/sign-in')
def set_(request):
    return render(request, 'python-course/12-set.html')
@login_required(login_url='/users/sign-in')
def if_(request):
    return render(request, 'python-course/13-if.html')

@login_required(login_url='/users/sign-in')
def funksiya(request):
    return render(request, 'python-course/14-funksiya.html')

@login_required(login_url='/users/sign-in')
def while_(request):
    return render(request, 'python-course/15-while.html')
@login_required(login_url='/users/sign-in')
def massiv(request):
    return render(request, 'python-course/16-massiv.html')
@login_required(login_url='/users/sign-in')
def sinfobject(request):
    return render(request, 'python-course/17-sinfobject.html')
@login_required(login_url='/users/sign-in')
def meros(request):
    return render(request, 'python-course/18-meros.html')
@login_required(login_url='/users/sign-in')
def modul(request):
    return render(request, 'python-course/19-modul.html')
@login_required(login_url='/users/sign-in')
def data(request):
    return render(request, 'python-course/20-data.html')
@login_required(login_url='/users/sign-in')
def json(request):
    return render(request, 'python-course/21-json.html')
@login_required(login_url='/users/sign-in')
def try_(request):
    return render(request, 'python-course/22-try.html')
@login_required(login_url='/users/sign-in')
def fayl(request):
    return render(request, 'python-course/23-fayl.html')

def test(request):
    return render(request, 'test/1-test.html')


def contact(request):
    if request.method == 'POST':
        data = request.POST
        Contact.objects.create(name=data['name'],
                       email=data['email'],
                       number=data['number'],
                       course=data['course'],
                       gender=data['gender']
                       )
        return redirect('/')