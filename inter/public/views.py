from django.shortcuts import render,redirect
from .models import manage,UserProfile
from django.contrib.auth.models import User
from django.contrib.auth import login as authlogin,logout as authlogout,authenticate
from django.contrib.auth.hashers import check_password
# Create your views here.

def home(request):
    print('hello')
            

    
    print("waitt")
    return render(request,'home.html')


def login(request):

    if request.POST:
        uname=request.POST.get('uname')
        pwd=request.POST.get('pwd')
        user=authenticate(username=uname,password=pwd)
        print(request.user)
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        if user:
            authlogin(request,user)
            print(request.user)
            userpro=UserProfile.objects.filter(user=user).exists()
            if userpro:
                userpro=UserProfile.objects.get(user=user)
                print("Heyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy")
                print(userpro.user_type)
                return redirect(manage_site)
        
    return render(request,'login.html')



def reg(request):
    print(request.method)
    if request.POST:
        print(request.POST)
        print(request.POST.get('uname'))
        print("$@##$#$$$$$$$$$$$$$$$$$")
        uname=request.POST.get('uname')
        pwd=request.POST.get('pwd')
        print(uname,pwd)
        checkexist=User.objects.filter(username=uname).exists()
        print(checkexist)
        flag=0
        if checkexist:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            checkexist=User.objects.get(username=uname)
            if check_password(pwd,checkexist.password):
                print("existtttttttttt")
                flag=1
        if flag==0:
            reg=User.objects.create_user(username=uname,password=pwd)
            uprofile=UserProfile(user=reg,user_type='test')
            uprofile.save()
            
            return redirect(login)
    return render(request,'reg.html')

def manage_site(request):
    print("rr",request)
    data={}
    manage_list=manage.objects.all()
    data['list']=manage_list
    print(manage_list)
    if 'submit' in request.POST:
        print('file checkkkkk')
        print(request.FILES)
        title=request.POST.get('title')
        des=request.POST.get('des')
        img=request.FILES.get('img')

        cobj=manage.objects.create(title=title,description=des,img=img)
        # cobj=manage(title=title,description=des)
        # cobj.save()
        return redirect(manage_site)
    
    if 'action' in request.GET:
        action=request.GET['action']
        id=request.GET['id']
    else:
        action=None
    print(request.GET)
    print(action)
    if action=='delete':
        dobj=manage.objects.filter(pk=id)
        dobj[0].delete()
        return redirect(manage_site)
    if action=='update':
        print('enter update')
        q='select * from public_manage where id=%s'%(id)
        print(q)
        upobj=manage.objects.raw(q)
        print(upobj)
        print(list(upobj))
        upobj=list(upobj)
        data['updater']=list(upobj)
        upobj=manage.objects.filter(pk=id)
        print(upobj)
        # print(data['updater'][0].title)
        

    if 'update' in request.POST:
        title=request.POST.get('title')
        des=request.POST.get('des')
        img=request.FILES.get('img')
        # upobj[0].title=title
        # upobj[0].save()
        print("$$$$$$$$$$$^^^^^^^^^^^^^^^^^W")
        print(upobj)
        print(upobj[0])
        upobj=upobj[0]

        print(upobj)
        print(upobj.title)
        upobj.title=title
        upobj.description=des
        upobj.img=img
        upobj.save()
        print(upobj.title)
        return redirect(manage_site)

    return render(request,'manage.html',data)