from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin

from apps.models import CustomUser, Service, Portfolio, Feedback, Contact


@admin.register(CustomUser)
class UserAdmin(ModelAdmin):
    pass


@admin.register(Service)
class ServiceAdmin(ModelAdmin):
    pass


@admin.register(Portfolio)
class PortfolioAdmin(ModelAdmin):
    pass


@admin.register(Feedback)
class FeedbackAdmin(ModelAdmin):
    pass


@admin.register(Contact)
class FeedbackAdmin(ModelAdmin):
    pass
