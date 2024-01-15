from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm

# django.contrib.auth.models built in package


#for messages framework
from django.contrib import messages

def signup_page(request):
    if request.method == "POST":
        username = request.POST.get("uname")
        firstname = request.POST.get("fname")
        lastname = request.POST.get("lname")
        password = request.POST.get("passw")
        con_password = request.POST.get("confirm_pass")
        Email = request.POST.get("email")
        
        if (password!=con_password):
            messages.error(request, "Password and confirm password should be same")
            return redirect('/allibaba/home')
        
        user_object = User.objects.create_user (username, Email, password)
        user_object.first_name = firstname
        user_object.last_name = lastname

        user_object.save()
        messages.success(request,"User Updated Successfully")
        return redirect('/allibaba/home')
          
    return render(request, 'signup.html')
   

def login_page(request):
    if request.method == "POST":
        uname = request.POST.get("uname")
        passw = request.POST.get("passw")
        
        print(uname, "-----",passw)
        # authenticate
        
        my_user = authenticate(username = uname, password = passw)
        
        if my_user is not None: #credentials founds
            login(request, my_user)
            ename = my_user.first_name + " " + my_user.last_name
            # ename = my_user.username
            context = {"uname":ename}
            print (context)
            return render (request, 'dashboard.html',context)
        
        else:
            messages.error(request,"Credential not found")
            return render (request,"login.html")
        
    return render(request, 'login.html')


def logout_page(request):
    logout(request)
    messages.success(request, "Logout successfull")
    return redirect ('/allibaba/login')


def forget_password (request):
    return render (request, 'forget_password.html')



# change password
def change_password(request, username):
    COD_black = User.objects.get(username=username)
    context = {"change_passw": COD_black}

    if request.method == "POST":
        old_password = request.POST.get("old_passw")
        new_password = request.POST.get("new_passw")
        con_password = request.POST.get("con_passw")

        if old_password and new_password == con_password:
            user = authenticate(username=username, password=old_password)

            if user is not None:
                user.set_password(new_password)
                user.save()
                messages.success(request, "Password updated successfully")
            else:
                messages.error(request, "Incorrect old password")
        else:
            messages.error(request, "New password and confirmation do not match")

    return render(request, 'change_password.html', context)



