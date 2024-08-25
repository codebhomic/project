from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.urls import reverse
from user.tokens import account_activation_token

def send_activation_email(user,user_type, request):
    token = account_activation_token.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    activation_link = request.build_absolute_uri(reverse('activate', kwargs={'uidb64': uid, 'token': token,'user_type':user_type}))

    subject = 'Activate your account'
    message = render_to_string('account_activation_email.html', {
        'user': user,
        'activation_link': activation_link,
    })
    send_mail(subject, message, 'from@example.com', [user.email])
