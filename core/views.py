from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from product.models import Product
from product.models import Category
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView as AuthLoginView
from .forms import SignupForm, LoginForm
from django.contrib import messages

def home(request):
    products = Product.objects.filter(is_sold=False)
    latest_products = Product.objects.order_by('-date_added')[:3]
    categories = Category.objects.all()
    return render(request, 'core/home.html', {
        'categories': categories,
        'products': products,
        'latest_products': latest_products,
    })

class LoginView(AuthLoginView):
    template_name = 'core/login.html'
    authentication_form = LoginForm

    def form_valid(self, form):
        login(self.request, form.get_user())
        return redirect('core:home')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:login')  # Redirect to login page after successful signup
    else:
        form = SignupForm()
    
    return render(request, 'core/signup.html', {'form': form})

def logout_user(request):
    logout(request)
    messages.success(request, "You Were Logged Out")
    return redirect('core:home')