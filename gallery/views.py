

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PhotoUploadForm
from .models import Photo
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
#from django.views.generic import View





def Signup(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']

        data = User.objects.create_user(username=username, email=email,password=password)
        data.save()
        return redirect('Login')
    
    return render (request, "Register.html")

def Login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user= authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            #messages.success(request, "Successfully Logged In")
            return redirect('upload_photo')
        else:
            messages.error(request, "Username or password is incorrect!!!")
        
    return render (request, "Log-in.html")



def LogoutPage(request):
    

        logout(request)
        return redirect('Login')



@login_required
def upload_photo(request):
    if request.method == 'POST':
        form = PhotoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = request.user
            photo.save()
            return redirect('upload_photo')
    else:
        form = PhotoUploadForm()
    photos = Photo.objects.filter(user=request.user)
    return render(request, 'upload_photo.html', {'photos': photos ,'form': form})

#@login_required
#def my_photos(request):
   # photos = Photo.objects.filter(user=request.user)
    #return render(request, 'my_photos.html', {'photos': photos})

def user_photos(request):
    if request.method == 'GET' and 'username' in request.GET:
        username = request.GET['username']
        try:
            user = User.objects.get(username=username)
            photos = Photo.objects.filter(user=user)
            return render(request, 'user_photos.html', {'photos': photos, 'user': user})
        except User.DoesNotExist:
            return render(request, 'user_photos.html', {'error': 'User does not exist.'})
    return render(request, 'user_photos.html')

