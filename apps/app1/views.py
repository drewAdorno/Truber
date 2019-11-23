from django.shortcuts import render, redirect
from django.contrib import messages
from . models import *
import bcrypt

def validate(request):
    errors=User.objects.validator(request.POST)
    if len(errors) > 0:
        for key,value in errors.items():
            messages.error(request, value)
        return (True)
    return(False)

def cust_index(request):
    if 'loggedInUser_id' not in request.session:
        request.session['loggedInUser_id']=""
        return render(request,'app1/cust_reg_log.html')
    elif request.session['loggedInUser_id']=="":
        return render(request,'app1/cust_reg_log.html')
    return redirect('/success')

def cust_register(request):
    if(validate(request)):                  #if there are any post validation errors redirect with error messaging
        return redirect('/cust_home')
    else:
        hashed_pw=bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())   #putting hashed pw into db
        User.objects.create(email=request.POST['email'], password=hashed_pw)            #creating new user object
        
        loggedInUser=User.objects.get(email=request.POST['email'])                      #adding user to session (Loging in)
        request.session['loggedInUser_id']=loggedInUser.id

        return redirect('/success')

def cust_login(request):
    emailFilter=User.objects.filter(email=request.POST['email'])
    if(len(emailFilter)):
        user=emailFilter[0]
    else:
        request.session['errors'].append("Email Address doesn't exist")
        return redirect('/cust_home')

    if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
        request.session['loggedInUser_id']=user.id
        return redirect('/success')
    else:
        return redirect('/cust_home')

def success(request):
    if 'loggedInUser_id' not in request.session or request.session['loggedInUser_id']=="":
        return(redirect('/cust_home'))
    return redirect('/home')

#------------------------------------------------------------------------------------------------------------------------------------------------------

def driver_index(request):
    if 'loggedInDriver_id' not in request.session:
        request.session['loggedInDriver_id']=""
        return render(request,'app1/driver_reg_log.html')
    elif request.session['loggedInDriver_id']=="":
        return render(request,'app1/driver_reg_log.html')
    return redirect('/driver_success')

def driver_register(request):                               
    
    if request.POST['password'] != request.POST['confirm_password']:
        return redirect('/driver_home')
    
    hashed_pw=bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())  
    Driver.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=hashed_pw)            
    loggedInDriver=Driver.objects.get(email=request.POST['email'])                    
    request.session['loggedInDriver_id']=loggedInDriver.id

    return redirect('/driver_success')

def driver_login(request):
    emailFilter=Driver.objects.filter(email=request.POST['email'])
    if(len(emailFilter)):
        user=emailFilter[0]
    else:
        return redirect('/driver_home')

    if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
        request.session['loggedInDriver_id']=user.id
        return redirect("/driver_success")
    else:
        return redirect('/driver_home')

def driver_success(request):
    if 'loggedInDriver_id' not in request.session or request.session['loggedInDriver_id']=="":
        return(redirect('/cust_home'))
    return redirect('/home/driver')

def logout(request):
    request.session.clear()
    return redirect('/cust_home')