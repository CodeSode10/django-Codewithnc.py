from django.shortcuts import render, redirect
from .form import *
from .models import*
from django.conf import settings
from django.core.mail import send_mail
from django.core.paginator import Paginator

def home(request):
    try:
        data = {
            'blogs': BlogModel.objects.all().order_by('-id')[0:4],
            'courses': CoursePartModel.objects.all().order_by('-id')[0:4],
            'services': ServiceModel.objects.all().order_by('-id')[0:6],
            'title': 'Home'
        }
    except Exception as e:
        print(e)
    return render(request, 'index.html', data)


def about(request):
    data = {
        'title': 'About'
    }
    return render(request, 'about.html', data)


def contact(request):
    try:
        data = {
            # 'user': User,
            'title': 'Contact'
        }

        if request.method == 'POST':
            form = ContactModel()
         
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            created_at = request.POST.get('created_at')
    
            form.name = name
            form.email = email
            form.subject = subject
            form.message = message
            form.created_at = created_at
            form.save()

            #email sending
            subject = 'CodeWithNc Contact Submition Auto Reply'
            message = f'Dear {name},\n\nIts just a mail to inform you that your message is recieved, no need to reply'
            email_from = settings.EMAIL_HOST_USER
            email_to = [email]

            send_mail(subject, message, email_from, email_to, fail_silently=False)
             
            return render(request, 'contact.html', data)

    except Exception as e:
        print(e)

    return render(request, 'contact.html', data)


def courses(request):
    allCourses = CoursePartModel.objects.all()
    #pagination
    paginator = Paginator(allCourses, 6)
    page_number = request.GET.get('page')
    allCoursesFinal = paginator.get_page(page_number)

    data = {
        'user': User,
        'courses': allCoursesFinal,
        'title': 'Course Videos'
    }
    return render(request, 'courses.html', data)

def courseSingle(request, slug):
    try:
        data = {
            'course': CoursePartModel.objects.get(slug = slug),
            'title': 'Course Single'
        }
    except Exception as e:
        print(e)
    return render(request, 'course-single.html', data)

def Ulogin(request):
    try:
        data = {
            'title': 'User Login'
        }
    except Exception as e:
        print(e)
    return render(request, 'login.html', data)


def signup(request):
    data = {
        'title': 'User SignUp'
    }
    return render(request, 'signup.html', data)


def registerAd(request):
    data = {
        'title': 'Admin Signup'
    }
    return render(request, 'register.html', data)


def accessAd(request):
    data = {
        'user': User.objects.get(),
        'title': 'Admin Login'
    }
    return render(request, 'access.html', data)


def blog(request):
    allBlogs = BlogModel.objects.all()
    #pagination
    paginator = Paginator(allBlogs, 6)
    page_number = request.GET.get('page')
    allBlogsFinal = paginator.get_page(page_number)

    data = {
        'blogs': allBlogsFinal,
        'title': 'Blogs'
    }
    return render(request, 'blog.html', data)


def blogSingle(request, slug):
    try:
        data = {
            'blog': BlogModel.objects.get(slug=slug),
            'title': 'Single-Blog'
        }
    except Exception as e:
        print(e)
    return render(request, 'blog-single.html', data)


def recent(request):
    data = {
        'recent': Recent.objects.all().order_by('-id'),
        'title': 'Recent Notification'
    }
    return render(request, 'recent.html', data)


def admin(request):
    data = {
        'form': BlogForm,
        'title': 'Admin Panel'
    }
    # content =''
    try:
        if request.method == 'POST':
            form = BlogForm(request.POST)
            image = request.FILES['image']
            title = request.POST.get('title')
            user = request.user

            if form.is_valid():
                content = form.cleaned_data['content']

            BlogModel.objects.create(
                user = user, image = image,
                title = title, content = content
            )

            return redirect('/admin/')
         
    except Exception as e:
        print(e)

    return render(request, 'admin.html', data)


def varifyAd(request, token):
    try:
        profile_obj = Profile.objects.filter(token = token).first()

        if profile_obj:
            profile_obj.is_varified = True
            profile_obj.save()
        
            return redirect('/access/')
        else:
            profile_obj.is_varified = False

    except Exception as e:
        print(e)