from django.utils.text import slugify
import string
import random


def generate_random_string(N):
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
    return res


def generate_slug(text):
    new_slug = slugify(text)

    from Home.models import BlogModel
    if BlogModel.objects.filter(slug = new_slug).first():
        return generate_slug(text + generate_random_string(5))
    
    from Home.models import CourseModel
    if CourseModel.objects.filter(slug = new_slug).first():
        return generate_slug(text + generate_random_string(5))
    
    from Home.models import CoursePartModel
    if CoursePartModel.objects.filter(slug = new_slug).first():
        return generate_slug(text + generate_random_string(5))
    
    from Home.models import ServiceModel
    if ServiceModel.objects.filter(slug = new_slug).first():
        return generate_slug(text + generate_random_string(5))
    
    return new_slug


# email varification
# from django.conf import settings
# from django.core.mail import send_mail
# def send_varify_mail_to_user(email, token):
#     subject = f'Dear CodeWithNc user, your account needs to be varified.'
#     message = f'To varify your account tap on "Varify" button or paste & browse the link on any of browsers. : http://127.0.0.1:8000/varify/{token}/'
#     email_from = settings.EMAIL_HOST_USER
#     recipient_list = [email]
#     send_mail(subject, message, email_from, recipient_list)
#     return True
