from django.shortcuts import HttpResponse,render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import auth

def index(request):
    """
    index page
    :param request:
    :return:
    """
    if request.method=="GET":
        return render(request, 'index.html')
    email = request.POST.get("email")
    password = request.POST.get("password")
    # return HttpResponse(email+password)
    user_obj = auth.authenticate(username=email, password=password)
    print(user_obj.username)
    if not user_obj:
        return redirect("/calendar_app/login/")
    else:
        auth.login(request, user_obj)
        path = request.GET.get("next") or "/calendar_app/welcome/"
        return redirect(path)

        pass

def create_account(request):
    """
    create account page
    :param request:
    :return:
    """
    if request.method=="GET":
        return render(request, 'create_account.html')
    first_name = request.POST.get("firstname")
    surname = request.POST.get("surname")
    email = request.POST.get("email")
    password = request.POST.get("password")
    if User.objects.filter(username=email):

        return render(request,"/calendar_app/createaccount/",{'msg':'email has been registered'})
        # return redirect("/toDoer/createaccount/",{'msg':'email has been registered'})
    else:
        new_user = User.objects.create_user(username=email, password=password,first_name=first_name,last_name=surname)
        new_user.save()
            # return HttpResponse(111)

def logout(request):
    """
    Logs the user out
    :param request:
    :return:
    """
    auth.logout(request)
    return render(request, "index.html")

def welcome(request):
    '''

    :param request:
    :return:
    '''

    user_id=request.COOKIES.get('sessionid')
    current_user = request.user
    username=current_user.username
    first_name=current_user.first_name
    last_name=current_user.last_name
    return render(request, 'welcome.html', {'username': username,'first_name':first_name})


def postAddTask(request):
    id_token = request.session['uid']
    return HttpResponse(id_token)




# Create your views here.
