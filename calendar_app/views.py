from django.contrib.auth import login, authenticate,logout
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from calendar_app.models import Events

def index(request):
    if request.method == "GET":
        return render(request, 'registration/login.html')
    email = request.POST.get("email")
    password = request.POST.get("password")
    user = authenticate(username=email, password=password)
    if user is not None:
        login(request, user)
        return redirect('/')
    else:
        return render(request, 'index.html', {'msg':'wrong password'})

@login_required
def welcome(request):
    '''
    index pages.
    :param request:
    :return:
    '''
    current_user = request.user
    username=current_user.username
    first_name=current_user.first_name
    last_name = current_user.last_name
    records = Events.objects.filter(user=current_user)
    return render(request, 'welcome.html', locals())


def create_account(request):
    """
    create account page
    :param request:
    :return:
    """
    if request.method=="GET":
        return render(request, 'create_account.html')
    else:
        first_name = request.POST.get("firstname")
        surname = request.POST.get("surname")
        email = request.POST.get("email")
        password = request.POST.get("password")
        if User.objects.filter(username=email):
            return render(request,'create_account.html',{'msg':'email has been registered'})
        else:
            new_user = User.objects.create_user(username=email, password=password,first_name=first_name,last_name=surname)
            new_user.save()
            user = authenticate(username=email, password=password)
            login(request, user)
            return redirect('/')

@login_required
def addEvents(request):
    user=request.user
    events=request.POST.get("Events")
    date=request.POST.get("date")
    startTime=request.POST.get("starttime")
    endTime=request.POST.get("endtime")
    Events.objects.create(
        user=user,
        date=date,
        event=events,
        start_time=startTime,
        end_time=endTime
    )
    return redirect('/')

@login_required
def deleteEvents(request):
    if request.method == 'POST':
        id = request.POST['delete_val']
        Events.objects.filter(id=id).delete()
    return redirect('/')

@login_required
def editEvents(request):
    id = request.POST.get("ID")
    events=request.POST.get("Events")
    date=request.POST.get("date")
    startTime=request.POST.get("starttime")
    endTime=request.POST.get("endtime")
    Events.objects.filter(id=id).update(
        date=date,
        event=events,
        start_time=startTime,
        end_time=endTime
    )
    return redirect('/')

@login_required
def searchEvents(request):
    if request.method == 'POST':
        title = request.POST['search']
        user = request.user
        records = Events.objects.filter(user=user, event=title)
        return render(request, 'welcome.html', locals())
    return redirect('/')

@login_required
def shareEvents(request):
    if request.method == 'POST':
        target_user=request.POST['shareuser']
        date = request.POST['shareeventsdate']
        title = request.POST['shareeventstitle']
        start_time = request.POST['shareeventsstarttime']
        end_time = request.POST['shareeventsendtime']
        user =User.objects.get(username=target_user)
        Events.objects.create(
            user=user,
            date=date,
            event=title,
            start_time=start_time,
            end_time=end_time
        )
    return redirect('/')

@login_required
def settingsInfo(request):
    first_name = request.POST.get("fname")
    surname = request.POST.get("sname")
    email = request.POST.get("email")
    user = User.objects.get(username=email)
    user.first_name = first_name
    user.last_name = surname
    user.save()
    return redirect('/')

@login_required
def logout_view(request):
    """
    Logs the user out
    :param request:
    :return:
    """
    logout(request)
    return render(request, 'logged_out.html', locals())

# Create your views here.
