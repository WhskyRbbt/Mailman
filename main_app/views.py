from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from .forms import SignUpForm, PackageForm
from .models import Package

def login(request):
    return render(request, "../templates/registration/login.html")

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            username = authenticate(username=username, password=raw_password)
            login(request)
            return redirect("/login/")
    else:
        form = SignUpForm()
    return render(request, "registration/signup.html", {"form": form})

@login_required
def home(request):
    packages = Package.objects.all()
    return render(request, "main_app/home.html", { "packages": packages })

@login_required
def profile(request):
    print(request.user)
    packages = Package.objects.filter(users__username = request.user)
    return render(request, "main_app/profile.html", { "packages": packages, "user": request.user })

@login_required
def package_detail(request, pkg_id):
    package = Package.objects.get(id=pkg_id)
    shipper = package.users.first()
    return render(request, "main_app/detail.html", { "package": package, "shipper": shipper })

@login_required
def assoc_driver(request, pkg_id, user_id):
    Package.objects.get(id=pkg_id).users.add(user_id)
    return redirect("/profile/")

@login_required
def package_create(request):
    if request.method == "POST":
        user_id = request.POST["users"]
        user = User.objects.get(id=user_id)
        form = PackageForm(request.POST)
        new_package = form.save(commit=False)
        new_package.save()
        package = Package.objects.get(id=new_package.id)
        package.users.add(user)
        return redirect("/profile/")
    else:
        return render(request, "main_app/package_form.html")

class PackageUpdate(UpdateView):
    model = Package
    fields = ["length", "width", "height", "weight", "is_fragile"]
    success_url = "/profile/"
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class PackageDelete(DeleteView):
    model = Package
    success_url = "/profile/"
<<<<<<< HEAD

def profile(request):
    print(request.user)
    packages=Package.objects.filter(users__username = request.user)
    return render(request, 'main_app/profile.html', { "packages": packages, "user": request.user })

# @login_required
def package_detail(request, pkg_id):
    packages = Package.objects.get(user = request.user)
    return render(request, 'main_app/detail.html', { "packages": packages })


@login_required
def package_detail(request, pkg_id):
    package = Package.objects.get(id=pkg_id)
    return render(request, 'main_app/detail.html', {"package": package})


@login_required
def assoc_driver(request, pkg_id, user_id):
    user = request.user
    Package.objects.get(id=pkg_id).users.add(user_id)
    return redirect('/profile/')
=======
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
>>>>>>> a1830e78870a1f68788bb444d06d5d43862aef6b
