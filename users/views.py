from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, Http404
from .models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode

from apps.utils.token import account_activation_token
from shared.decorators import anonymous_required
from shared.utils.send_to_email import send_email
from .forms import UserForm, ProfileForm, LoginForm, RegisterForm
from django.shortcuts import get_object_or_404
from main.models import Test, CheckTest

# Create your views here.

@anonymous_required(redirect_url='/')
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.data.get('email')
            password = form.data.get('password')
            user_ = User.objects.filter(email=email).first()
            user = authenticate(email=email, password=password)
            if user_ and not user_.is_active:
                messages.add_message(request,
                                     level=messages.WARNING,
                                     message='user is not active'
                                     )
            elif user:
                login(request, user)
            else:
                messages.add_message(request,
                                     level=messages.ERROR,
                                     message='email or password wrong'
                                     )
                return render(request, 'auth/login.html')
            return redirect('home')
    return render(request, 'auth/login.html')


@anonymous_required(redirect_url='/')
def register_view(request):
    context = {}
    if request.method == 'POST':
        forms = RegisterForm(request.POST)
        if forms.is_valid():
            user = forms.save()
            # User.objects.create(user=user)
            # Profile.objects.create(user=user)
            send_email(request, forms.data.get('email'), type_='register')
            return redirect('confirm_your_email')
        else:
            context['errors'] = forms.errors
    return render(request, 'auth/register.html', context)

def register_activate_email(request, uid, token):
    try:
        uid = force_str(urlsafe_base64_decode(uid))
        user = User.objects.get(pk=uid)
    except Exception as e:
        print(e)
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('login')
    else:
        return HttpResponse('Activate link is expired')

def confirm_your_email(request):
    return render(request, 'auth/message.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url="login")
def update_user(request):
    user = request.user
    form = UserForm(instance=user)
    profileForm = ProfileForm(instance=user.profile)
    if request.method == "POST":
        profileForm = ProfileForm(instance=user.profile, data=request.POST, files=request.FILES)
        form = UserForm(instance=user, data=request.POST)
        if form.is_valid() and profileForm.is_valid():
            form.save()
            profileForm.save()
            return redirect('profile', user.username)
        else:
            return render(request, "users/user_update.html", {'form':form, "profileForm":profileForm})
    return render(request, "users/user_update.html", {'form':form, "profileForm":profileForm})


def profile(request, username):
    # user = User.objects.get(id=user_id)
    user = get_object_or_404(User, username=username)
    if user.profile.anonym == False or user == request.user: 
        number_of_test = Test.objects.filter(author=user).count()
        check_tests = CheckTest.objects.filter(student=user)
        number_of_checktests = check_tests.count()
        tests = []
        for checktest in check_tests:
            if not checktest.test in tests:
                tests.append(checktest.test)
                
        context = {
            "user":user,
            "number_of_tests":number_of_test,
            "number_of_checktests":number_of_checktests,
            'tests':tests,
            "checktests":check_tests
        }
        return render(request, 'users/profile.html', context)
    else:
        raise Http404("Bu user yo'q")