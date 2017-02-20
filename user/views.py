import json

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from error import HttpError500
from user.models import UserDetails
import  logging
logger = logging.getLogger(__name__)

def login(request):
    # TODO : Redirect user if already logged in
    return render(template_name="user/login.html", request=request)

def register(request):
    # TODO : Redirect user if already logged in
    return render(template_name="user/register.html", request=request)

def logout(request):
    del request.session["userid"]
    del request.session["username"]

    return HttpResponseRedirect("/Order/")

def authenticate(request):
    username = request.POST.get("username")
    password = request.POST.get("password")

    user = UserDetails.objects.get(username=username)

    if user is not None and user.password == password:
        request.session["userid"] = user.userid
        request.session["username"] = user.name
        if user.user_type == UserDetails.USER_TYPE_CUSTOMER:
            return HttpResponse(json.dumps({
                "status": "success",
                "redirectUrl": "/Order/"
            }))
        elif user.user_type == UserDetails.USER_TYPE_OFFICE:
            return HttpResponse(json.dumps({
                "status": "success",
                "redirectUrl": "/Kitchen/"
            }))
    else:
        return HttpError500(json.dumps({
            "status": "error"
        }))


def newRegister(request):
    name = request.POST.get('name')
    username = request.POST.get('username')
    password = request.POST.get('password')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    address = request.POST.get('address')
    logger.warning(">>>>>>>>>>>>"+str(name))
    newUser = None
    try:
        newUser = UserDetails.objects.get(username=username)
        return HttpError500(json.dumps({
            "status": "Already registered..."
        }))
    except:
        newUser = UserDetails(
            username= username,
            password = password,
            email = email,
            phone = phone,
            address = address,
            user_type = UserDetails.USER_TYPE_CUSTOMER,
            name = name
        )
        newUser.save()
        request.session["userid"] = UserDetails.objects.get(username=username).userid
        request.session["username"] = UserDetails.objects.get(username=username).name
        return HttpResponse(json.dumps({
            "status": "success",
            "redirectUrl": "/Order/"
        }))