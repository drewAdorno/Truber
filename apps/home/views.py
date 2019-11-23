from django.shortcuts import render, redirect
from geopy.distance import geodesic
from geopy.geocoders import Nominatim
from .. app1.models import User,Driver
from . models import Pickup

def index(request):
    return render(request, 'home/index.html')

def searchDrivers(request, lat, lng):
    user=User.objects.get(id=request.session['loggedInUser_id'])
    user.lat=lat
    user.lng=lng
    user.save()
    my_coords=(lat,lng)
    foundDriver=findDriver(request, my_coords)
    if foundDriver == 0:
        context={
            'message':"No Drivers are currently avaliable"
        }
        return render(request, 'home/index.html', context)
    context={
        'message':"Found Driver!, Waiting for Driver to respond",
        'waiting':1
    }
    return render(request, 'home/index.html', context)

def address_to_coords(request): #TODO
    geolocator=Nominatim()
    address=""
    
    for key,value in request.POST:
        address+=value
    coords=geolocator.geocode(address)
    pickup=findDriver(request, coords)
    if pickup == 0:
        context={
            'message':"No Drivers are currently avaliable, since no queue has been implemented yet, keep clicking find driver"
        }
        return render(request, 'home/index.html', context)
    context={
        'pickup':pickup
    }
    return render(request, 'home/pickup.html', context)

def findDriver(request, my_coords):
    allDrivers=Driver.objects.all().filter(status=1)
    for driver in allDrivers:
        driver_coords=(driver.lat, driver.lng)
        if (geodesic(my_coords, driver_coords).miles) <=5:
            foundDriver=Driver.objects.get(id=driver.id)
            user=User.objects.get(id=request.session['loggedInUser_id'])
            user.status=0
            user.save()
            pickup=Pickup.objects.create(Driver=foundDriver, User=user)
            return(pickup)
    return(0)
def check_response(request):
    user=User.objects.get(id=request.session['loggedInUser_id'])
    if user.status:
        context={
            'pickup':Pickup.objects.get(User=user),
            'skip':0
        }
        return render(request, 'home/user_pickup.html', context)
    else:
        context={
        'message':"Found Driver!, Waiting for Driver to respond",
        'waiting':1
    }
        return render(request, 'home/index.html', context)
def dropOff_address(request):
    pickup=Pickup.objects.get(User=User.objects.get(id=request.session['loggedInUser_id']))
    geolocator=Nominatim()
    address=f"{request.POST['street']} {request.POST['city']} {request.POST['state']}"
    coords=geolocator.geocode(address)
    pickup.dropOff_lng=coords.longitude
    pickup.dropOff_lat=coords.latitude
    pickup.save()
    context={
             'pickup':pickup,
             'skip':1
        }
    return render(request, 'home/user_pickup.html', context)
def update_loc(request):
    context={
            'pickup':Pickup.objects.get(User=User.objects.get(id=request.session['loggedInUser_id']))
        }
    return render(request,'home/user_pickup.html',context)

#-----------------------------------------------------------------------------------------------------------------------------------------------------

def driver_home(request):
    return render(request, 'home/driver_home.html')

def driver_online(request,lat,lng):
    driver=Driver.objects.get(id=request.session['loggedInDriver_id'])
    driver.status=1
    driver.lat=lat
    driver.lng=lng
    driver.save()
    return render(request, 'home/driver_online.html')

def driver_offline(request):
    driver=Driver.objects.get(id=request.session['loggedInDriver_id'])
    driver.status=0
    driver.lat=0
    driver.lng=0
    pickup=Pickup.objects.filter(Driver=driver)
    if pickup:
        pickup.delete()
    driver.save()

    return redirect('/home/driver')

def driver_find_new_requests(request):
    new_pickup=Pickup.objects.filter(Driver=Driver.objects.get(id=request.session['loggedInDriver_id']))
    print("Checking for new pickup request")
    if new_pickup:
        context={
            'pickup':new_pickup[0],
        }
        print("You have a new pickup request")
        return render(request, 'home/driver_online.html',context)
    else:
        return render(request, 'home/driver_online.html')

def driver_accepted(request):
    pickup=Pickup.objects.get(Driver=Driver.objects.get(id=request.session['loggedInDriver_id']))
    context={
        'pickup':pickup
    }
    user=Pickup.objects.get(User=pickup.User).User
    user.status=True
    user.save()
    return render(request, 'home/driver_pickup.html', context)

def driver_dropoff(request):
    pickup=Pickup.objects.get(Driver=Driver.objects.get(id=request.session['loggedInDriver_id']))
    context={
        'pickup':pickup
    }

    return render(request, 'home/driver_dropoff.html', context)

def driver_updateLoc(request, lat,lng):
    driver=Driver.objects.get(id=request.session['loggedInDriver_id'])
    driver.lat=lat
    driver.lng=lng
    driver.save()

    return redirect('/home/driver_accepted')

def driver_finished(request):
    return render(request, 'home/driver_finished.html')