import hashlib

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_GET
from django.views.decorators.http import require_POST

from models import Member, User, Photo
from forms import LoginForm
from forms import RegisterForm

# Create your views here.

def encrypt(plain):
    plain = str(plain)
    return hashlib.sha512(plain).hexdigest()


def new_user(userdata):
    username = userdata['username']
    password = encrypt(userdata['password'])
    email = userdata['email']
    name = userdata['name']
    birthday = userdata['birthday']
    intro = userdata['intro']
    phone = userdata['phone']
    # photo = Photo.objects.get(id=1)

    member = Member(username=username, password=password, email=email)
    member.save()

    User.objects.create(member=member, name=name, 
                    birthday=birthday, intro=intro, phone=phone)

def login_user(username, password):
    username = str(username)
    password = encrypt(password)
    members = Member.objects.filter(username=username, password=password)

    if not members:
        return None
    return members[0]


def get_signup(request):
    form = RegisterForm()
    return render(request, 'sign_up.html', {
            'form': form,
    })

def get_signin(request):
    form = LoginForm()
    return render(request, 'sign_in.html', {
            'form': form,
    })


def post_signup(request):
    form = RegisterForm(request.POST)
 
    if form.is_valid():
        userdata = {
            'username': form.cleaned_data['user'],
            'password': form.cleaned_data['passwd'],
            'email': form.cleaned_data['email'],
            'name': form.cleaned_data['name'],
            'birthday': form.cleaned_data['birthday'],
            'intro': form.cleaned_data['intro'],
            'phone': form.cleaned_data['phone']
        }
        print 'su', userdata['username']
        if login_user(userdata['username'], userdata['password']):
            return HttpResponseRedirect('/')
        print 'sign up success'
        new_user(userdata)
        return HttpResponseRedirect('signin')
    else:
        print 'form invalid'
    return HttpResponseRedirect('/')



def post_signin(request):
    form = LoginForm(request.POST)
    if form.is_valid():

        username = form.cleaned_data['user']
        password = form.cleaned_data['passwd']
   
        redirect_url = 'http://google.com'
        user = login_user(username, password)
        if user:
            request.session['user'] = username
            redirect_url = '/'
        else: # id not found
            pass
        return HttpResponseRedirect(redirect_url)
    return HttpRequestRedirect('/')

def sign_up(request):
    if request.method == 'GET':
        return get_signup(request)
    elif request.method == 'POST':
        return post_signup(request)

def sign_in(request):
    if request.method == 'GET':
        return get_signin(request)
    elif request.method == 'POST':
        return post_signin(request)

def sign_out(request):
    del request.session
    return HttpResponseRedirect('/')
