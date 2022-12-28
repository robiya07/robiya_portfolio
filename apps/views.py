from django.urls import reverse_lazy

from apps.forms import ContactForm
from apps.models import CustomUser

from django.views.generic import TemplateView, CreateView


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

