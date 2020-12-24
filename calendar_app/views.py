from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import HttpResponse,render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import auth
from calendar_app.models import Events


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
    last_name=current_user.last_name
    return HttpResponse(current_user.username)
    return render(request, 'welcome.html', {'username': username,'first_name':first_name})


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
            return redirect('/')









    #     return render(request, 'create_account.html')
    # first_name = request.POST.get("firstname")
    # surname = request.POST.get("surname")
    # email = request.POST.get("email")
    # password = request.POST.get("password")
    # if User.objects.filter(username=email):
    #
    #     return render(request,'create_account.html',{'msg':'email has been registered'})
    #     # return redirect("/toDoer/createaccount/",{'msg':'email has been registered'})
    # else:
    #     new_user = User.objects.create_user(username=email, password=password,first_name=first_name,last_name=surname)
    #     new_user.save()
    #     return render(request, 'index.html')


# @login_required
# def index(request):
#     """
#     index page
#     :param request:
#     :return:
#     """
#     email = request.POST.get("email")
#     password = request.POST.get("password")
#     # return HttpResponse(email+password)
#     user_obj = auth.authenticate(username=email, password=password)
#     if not user_obj:
#         return redirect("/calendar_app/login/")
#     else:
#         auth.login(request, user_obj)
#         # return redirect("/calendar_app/test/")
#         path = request.GET.get("next") or "/calendar_app/welcome/"
#         return redirect(path)

#
#
# def logout(request):
#     """
#     Logs the user out
#     :param request:
#     :return:
#     """
#     auth.logout(request)
#     return render(request, "index.html")
#
#
#
# @login_required
# def test(request):
#     Events.objects.create(email_address='xx@xx1',note='1111')
#     haha=Events.objects.get(email_address="xx@xx1")
#     return HttpResponse(haha)
#
# @login_required
# def postAddEvents(request):
#     Events.objects.create(email_address='xx@xx',note='111')
#     haha=Events.objects.get(email_address="xx@xx")
#     return HttpResponse(haha)
#     id_token = request.session['uid']
#     return HttpResponse(id_token)




# Create your views here.
