from django.shortcuts import render
from django.contrib import messages

from .models import (
    BLOG,
    REVIEW,
    
)

from  django.views import generic
from . forms import BlogForm, ContactForm, CreateUserForm, ReviewForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import redirect

def registerPage(request):
    context= None
    if request.user.is_authenticated:
        return redirect("main:home")
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Su Cuenta ha sido creada de forma Satisfactoria')

                return redirect('main:login')

        context= {'form':form}
        return render(request, 'main/signup.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect("main:home")
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("main:home")
            else:
                messages.info(request, 'Username OR password is incorrect')
        
        context ={}
        return render(request, 'main/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('main:login')


class IndexView(generic.TemplateView):
    template_name= "main/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs )
        reviews = REVIEW.objects.filter(is_active=True)
        blogs = BLOG.objects.filter(is_active=True)
        

        context["Reviews"] = reviews
        context["blogs"] = blogs

        return context

class BlogView(generic.ListView):
    model = BLOG
    template_name = "main/blog.html"
    paginate_by = 12

    def get_queryset(self):
        return super().get_queryset().filter(is_active = True)

class BlogDetailView(generic.DetailView):
    model = BLOG
    template_name = "main/blog-details.html"

class ReviewView(generic.ListView):
    model = REVIEW
    template_name = "main/categories.html"
    paginate_by = 20

    def get_queryset(self):
        return super().get_queryset().filter(is_active = True)

class ReviewDetailView(generic.DetailView):
    model = REVIEW
    template_name = "main/anime-details.html"

class BlogAddInfo(generic.FormView):
	template_name = "main/anime-watching.html"
	form_class = BlogForm
	success_url = "/"
	
	def form_valid(self, form):
		form.save()
		messages.success(self.request, 'Gracias por contribuir a la Comunidad con esta creación <3 te queremos mucho.')
		return super().form_valid(form)

class ReviewAddInfo(generic.FormView):
	template_name = "main/anime-watching2.html"
	form_class = ReviewForm
	success_url = "/"
	
	def form_valid(self, form):
		form.save()
		messages.success(self.request, 'Gracias por contribuir a la Comunidad con esta creación <3 te queremos mucho.')
		return super().form_valid(form)

# APARTADO PARA VISUALIZAR TUS MODELOS, EN ESTE CASO IndexView, BlogView, BlogDetailView, ReviewView, ReviewDetailView, BlogAddInfo & ReviewAddInfo