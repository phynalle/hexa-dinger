import hashlib

from django.shortcuts import render
from django.views.decorators.http import require_GET
from django.views.decorators.http import require_POST

from models import Member, User, Photo

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
    photo = Photo.objects.get(id=1)


    member = Member(username=username, password=password, email=email)
    member.save()

    User.objects.create(member=member, name=name, 
                    birthday=birthday, intro=intro, phone=phone, 
                    photo=photo)

def login_user(username, password):
    username = str(username)
    password = encrypt(password)
    members = Member.objects.filter(username=username, password=password)
    if not members:
        return None
    return members[0]


@require_GET
def show_sign_up():
    pass

@require_GET
def show_sign_in():
    pass



@require_POST
def sign_up():
    pass

@require_POST
def sign_in():
    username = 'pp';
    password = encrypt('343');
    
    query = Member.objects.filter(username=username)
    query.filter(password=password)

    print query


