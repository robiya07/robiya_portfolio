from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.urls import reverse_lazy

from apps.forms import ContactForm
from apps.models import CustomUser

from django.views.generic import TemplateView, CreateView

from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from apps.utils.tokens import account_activation_token
from django.contrib import messages


class MainView(CreateView):
    model = CustomUser
    template_name = 'apps/index.html'
    form_class = ContactForm
    success_url = reverse_lazy('index')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['user'] = CustomUser.objects.first()
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class ComponentsView(TemplateView):
    template_name = 'apps/components.html'


def activateEmail(request, user, to_email):
    mail_subject = 'Activate your user account.'
    message = render_to_string('apps/auth/template_activate_account.html', {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        'protocol': 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(request, f'Dear <b>{user}</b>, please go to you email <b>{to_email}</b> inbox and click on \
            received activation link to confirm and complete the registration. <b>Note:</b> Check your spam folder.')
    else:
        messages.error(request, f'Problem sending confirmation email to {to_email}, check if you typed it correctly.')


def activate(request, uidb64, token):
    User = get_user_model()
    try:

        uid = force_str(urlsafe_base64_decode(uidb64))  # uidb64='Tm9uZQ'
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True

        user.save()

        messages.success(request, 'Thank you for your email confirmation. Now you can login your account.')
        return redirect('index')
    else:
        messages.error(request, 'Activation link is invalid!')

    return redirect('index')
