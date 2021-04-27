from django.shortcuts import render,redirect,get_object_or_404
from django.db import IntegrityError
from django.contrib.auth import login,authenticate,logout
from DigiZiaApp.forms import *
from django.contrib.auth.forms import AuthenticationForm
from DigiZiaApp.models import *

def home(request):
    return render(request,'DigiZiaApp/home.html')

def into(request):
    return render(request,"DigiZiaApp/into.html")

def SignUpUser(request):
    if request.method == "GET":
        return render(request, 'DigiZiaApp/SignUpUser.html', {'form': SignUpForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], first_name=request.POST["first_name"],
                                                last_name=request.POST["last_name"], email=request.POST["email"],
                                                password=request.POST["password1"])
                user.save()
                login(request,user)
                return redirect(into)
            except IntegrityError:
                return render(request, 'DigiZiaApp/SignUpUser.html',
                              {'form': SignUpForm, 'error': 'this username has been taken!'})


        else:
            return render(request, 'DigiZiaApp/SignUpUser.html', {'form': SignUpForm , 'error': 'password didnt match.try again'})


def LoginUser(request):
    if request.method == "GET":
        return render(request,'DigiZiaApp/LoginUser.html',{"form":AuthenticationForm})
    else:
        user = authenticate(request,username=request.POST["username"],password=request.POST['password'])
        if user is None:
            return render(request, 'DigiZiaApp/LoginUser.html', {"form": AuthenticationForm,'error':'username and password didnt match.Try again!'})
        else:
            login(request,user)
            return redirect(into)

def LogOutUser(request):
    if request.method == 'POST':
        logout(request)
        return redirect(home)

#-------------------------------------------------------------------------------------




def product(request,digi_pk):
    phones = Phone.objects.all()
    laptops = Laptop.objects.all()
    books = Book.objects.all()
    cameras = Camera.objects.all()

    if digi_pk == "phone":
        return render(request, "DigiZiaApp/products/phone.html", {"phones":phones})

    elif digi_pk == "laptop":
        return render(request, "DigiZiaApp/products/laptop.html",{"laptops":laptops})

    elif digi_pk == "book":
        return render(request, "DigiZiaApp/products/book.html",{"books":books})

    elif digi_pk == "camera":
        return render(request, "DigiZiaApp/products/camera.html",{"cameras":cameras})

def each_brand(request,digi_pk,brand_pk):
    #phone_section:
    if digi_pk == 'phone':

        if brand_pk == "SAMSUNG":
            phones = Phone.objects.filter(brand="sam")
            if phones is None:
                return render(request, "DigiZiaApp/phonebrands/samsung.html", {"error": 'cannt find any product'})
            else:
                return render(request, "DigiZiaApp/phonebrands/samsung.html", {"phones": phones})

        elif brand_pk == "APPLE":
            phones = Phone.objects.filter(brand="apl")
            if phones is None:
                return render(request, "DigiZiaApp/phonebrands/apple.html", {"error": 'cannt find any product'})
            else:
                 return render(request, "DigiZiaApp/phonebrands/apple.html", {"phones": phones})

        elif brand_pk == "SHIOMI":
            phones = Phone.objects.filter(brand="shi")
            if phones is None:
                return render(request, "DigiZiaApp/phonebrands/shiomi.html", {"error": 'cannt find any product'})
            else:
                return render(request, "DigiZiaApp/phonebrands/shiomi.html", {"phones": phones})

        elif brand_pk == "HUAWEI":
            phones = Phone.objects.filter(brand="hoa")
            if phones is None:
                return render(request, "DigiZiaApp/phonebrands/huawei.html", {"error": 'cannt find any product'})

            return render(request, "DigiZiaApp/phonebrands/huawei.html", {"phones": phones})

        elif brand_pk == "NOKIA":
            phones = Phone.objects.filter(brand="nok")
            if phones is None:
                return render(request, "DigiZiaApp/phonebrands/nokia.html", {"error": 'cannot find any product'})
            else:
                return render(request, "DigiZiaApp/phonebrands/nokia.html", {"phones": phones})
    #laptop section
    if digi_pk == "laptop":

        if brand_pk == "SAMSUNG":
            laptops = Laptop.objects.filter(brand="sam")
            if laptops is None:
                return render(request, "DigiZiaApp/laptopbrands/samsung.html", {"error": 'cannot find any product'})
            else:
                return render(request, "DigiZiaApp/laptopbrands/samsung.html", {"laptops": laptops})

        elif brand_pk == "APPLE":
            laptops = Laptop.objects.filter(brand="apl")
            if laptops is None:
                return render(request, "DigiZiaApp/laptopbrands/apple.html", {"error": 'cannot find any product'})
            else:
                 return render(request, "DigiZiaApp/laptopbrands/apple.html", {"laptops": laptops})

        elif brand_pk == "ASUS":
            laptops = Laptop.objects.filter(brand="asu")
            if laptops is None:
                return render(request, "DigiZiaApp/laptopbrands/asus.html", {"error": 'cannot find any product'})
            else:
                return render(request, "DigiZiaApp/laptopbrands/asus.html", {"laptops": laptops})

        elif brand_pk == "LENOVA":
            laptops = Laptop.objects.filter(brand="len")
            if laptops is None:
                return render(request, "DigiZiaApp/laptopbrands/lenova.html/", {"error": 'cannot find any product'})

            return render(request, "DigiZiaApp/laptopbrands/lenova.html", {"laptops": laptops})

        elif brand_pk == "HP":
            laptops = Laptop.objects.filter(brand="hpp")
            if laptops is None:
                return render(request, "DigiZiaApp/laptopbrands/hp.html", {"error": 'cannot find any product'})
            else:
                return render(request, "DigiZiaApp/laptopbrands/hp.html", {"laptops": laptops})

        elif brand_pk == "DELL":
             laptops = Laptop.objects.filter(brand="del")
             if laptops is None:
                return render(request, "DigiZiaApp/laptopbrands/dell.html", {"error": 'cannot find any product'})
             else:
                return render(request, "DigiZiaApp/laptopbrands/dell.html", {"laptops": laptops})

        elif brand_pk == "MSI":
             laptops = Laptop.objects.filter(brand="msi")
             if laptops is None:
                return render(request, "DigiZiaApp/laptopbrands/msi.html", {"error": 'cannot find any product'})
             else:
                return render(request, "DigiZiaApp/laptopbrands/msi.html", {"phones": laptops})

        elif brand_pk == "MICROSOFT":
            laptops = Laptop.objects.filter(brand="mic")
            if laptops is None:
                return render(request, "DigiZiaApp/laptopbrands/microsoft.html", {"error": 'cannot find any product'})
            else:
                return render(request, "DigiZiaApp/laptopbrands/microsoft.html", {"laptops": laptops})

        elif brand_pk == "ACER":
            laptops = Laptop.objects.filter(brand="ace")
            if laptops is None:
                return render(request, "DigiZiaApp/laptopbrands/acer.html", {"error": 'cannot find any product'})
            else:
                return render(request, "DigiZiaApp/laptopbrands/acer.html", {"laptops": laptops})

    # book section
    if digi_pk == "book":

        if brand_pk == "ARTS $ PHOTOGRAPHY":
            books = Book.objects.filter(category="art")
            if books is None:
                return render(request, "DigiZiaApp/bookcategories/arts & photography.html", {"error": 'cannot find any product'})
            else:
                return render(request, "DigiZiaApp/bookcategories/arts & photography.html", {"books": books})

        elif brand_pk == "CHILDERENS BOOK":
            books = Book.objects.filter(category="chi")
            if books is None:
                return render(request, "DigiZiaApp/bookcategories/childerens book.html", {"error": 'cannot find any product'})
            else:
                return render(request, "DigiZiaApp/bookcategories/childerens book.html", {"books": books})

        elif brand_pk == "HISTORY":
            books = Book.objects.filter(category="his")
            if books is None:
                return render(request, "DigiZiaApp/bookcategories/history.html", {"error": 'cannot find any product'})
            else:
                return render(request, "DigiZiaApp/bookcategories/history.html", {"books": books})

        elif brand_pk == "ROMANCE":
            books = Book.objects.filter(category="rom")
            if books is None:
                return render(request, "DigiZiaApp/bookcategories/romance.html/", {"error": 'cannot find any product'})

            return render(request, "DigiZiaApp/bookcategories/romance.html", {"books": books})

        elif brand_pk == "TEENS & YOUNG ADULT":
            books = Book.objects.filter(category="tee")
            if books is None:
                return render(request, "DigiZiaApp/bookcategories/teens & young.html", {"error": 'cannot find any product'})
            else:
                return render(request, "DigiZiaApp/bookcategories/teens & young.html", {"books": books})

        elif brand_pk == "ALL CATEGORIES":
            books = Book.objects.all()
            if books is None:
                return render(request, "DigiZiaApp/bookcategories/all.html", {"error": 'cannot find any product'})
            else:
                return render(request, "DigiZiaApp/bookcategories/all.html", {"books": books})

# camera section
    if digi_pk == "camera":

        if brand_pk == "SAMSUNG":
            cameras = Camera.objects.filter(brand="sam")
            if cameras is None:
                return render(request, "DigiZiaApp/camerabrands/samsung.html", {"error": 'cannot find any product'})
            else:
                return render(request, "DigiZiaApp/camerabrands/samsung.html", {"cameras": cameras})

        elif brand_pk == "CANON":
            cameras = Camera.objects.filter(brand="can")
            if cameras is None:
                return render(request, "DigiZiaApp/camerabrands/canon.html", {"error": 'cannot find any product'})
            else:
                return render(request, "DigiZiaApp/camerabrands/canon.html", {"cameras": cameras})

        elif brand_pk == "NIKON":
            cameras = Camera.objects.filter(brand="nik")
            if cameras is None:
                return render(request, "DigiZiaApp/camerabrands/nikon.html", {"error": 'cannot find any product'})
            else:
                return render(request, "DigiZiaApp/camerabrands/nikon.html", {"cameras": cameras})

        elif brand_pk == "FUJIFILM":
            cameras = Camera.objects.filter(brand="fuj")
            if cameras is None:
                return render(request, "DigiZiaApp/camerabrands/fujifilm.html/", {"error": 'cannot find any product'})

            return render(request, "DigiZiaApp/camerabrands/fujifilm.html", {"cameras": cameras})

        elif brand_pk == "SONY":
            cameras = Camera.objects.filter(brand="son")
            if cameras is None:
                return render(request, "DigiZiaApp/camerabrands/sony.html", {"error": 'cannot find any product'})
            else:
                return render(request, "DigiZiaApp/camerabrands/sony.html", {"cameras": cameras})

        elif brand_pk == "SHIOMI":
            cameras = Camera.objects.filter(brand="shi")
            if cameras is None:
                return render(request, "DigiZiaApp/camerabrands/shiomi.html", {"error": 'cannot find any product'})
            else:
                return render(request, "DigiZiaApp/camerabrands/shiomi.html", {"cameras": cameras})
