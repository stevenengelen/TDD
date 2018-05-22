from django.shortcuts import redirect
from django.core.mail import send_mail
from django.contrib import messages
from accounts.models import Token
from django.core.urlresolvers import reverse
from django.contrib import auth, messages

# Create your views here.
def send_login_email(request) :
    email = request.POST['email']
    token = Token.objects.create(email = email)
    url = request.build_absolute_uri(reverse('login') + '?token=' + str(token.uid))
    message_body = f'Use this link to log in:\n\n{ url }'
    send_mail('Your login link for Superlists',
            message_body,
            'noreply@superlists', 
            [email])
    messages.success(request, "Check your email, we've sent you a link you can use to log in.")
    return redirect('/')

def login(request) :
    user = auth.authenticate(uid = request.GET.get('token'))
    if user :
        auth.login(request, user)
    return redirect('/')
'''
def logout(request) :
    print('-------------------------------------in accounts views logout------------------------------')
    print('I want to log out')
    pretty_request(request)
    auth.views.logout(request)
    print('-------------------------------------end accounts views logout------------------------------')
    return redirect('/')

def pretty_request(request):
    headers = ''
    for header, value in request.META.items():
        if not header.startswith('HTTP'):
            continue
        header = '-'.join([h.capitalize() for h in header[5:].lower().split('_')])
        headers += '{}: {}\n'.format(header, value)

    return (
        '{method} HTTP/1.1\n'
        'Content-Length: {content_length}\n'
        'Content-Type: {content_type}\n'
        '{headers}\n\n'
        '{body}'
    ).format(
        method=request.method,
        content_length=request.META['CONTENT_LENGTH'],
        content_type=request.META['CONTENT_TYPE'],
        headers=headers,
        body=request.body,
    )
'''
