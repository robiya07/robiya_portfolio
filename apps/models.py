from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# Create your models here.
from django.db.models import ImageField, TextField, CharField, DateField, JSONField, Model, ManyToManyField, RESTRICT, \
    ForeignKey, EmailField


class Service(Model):
    name = CharField(max_length=255)
    desc = TextField()

    def __str__(self):
        return self.name


class CustomUser(Model):
    first_name = CharField(max_length=255)
    last_name = CharField(max_length=255)
    image = ImageField(upload_to='user')
    bio = TextField()
    gender = CharField(max_length=255)
    birthday = DateField(null=True, blank=True)
    phone = CharField(max_length=255, null=True, blank=True)
    profession = CharField(max_length=255)
    telegram = CharField(max_length=255)
    instagram = CharField(max_length=255)
    mail = CharField(max_length=255)
    github = CharField(max_length=255)
    service = ManyToManyField(Service)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        # https: // github.com / robiya07
        if not self.github.startswith('https://github.com'):
            self.github = f'https://github.com/{self.github}'
        elif not self.github.startswith('http'):
            self.github = f'https://{self.github}'

        # https: // t.me / inspiring_sunset
        if not self.telegram.startswith('https://t.me'):
            self.telegram = f'https://t.me/{self.telegram.replace("@", "")}'
        elif not self.telegram.startswith('http'):
            self.telegram = f'https://{self.telegram}'

        super().save(force_insert, force_update, using, update_fields)

    @property
    def feedbacks(self):
        return self.feedback_set.all()

    @property
    def projects(self):
        return self.portfolio_set.all()

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Feedback(Model):
    u_firstname = CharField(max_length=255)
    u_lastname = CharField(max_length=255)
    u_image = ImageField(upload_to='user', default='default/avatar.jpg')
    text = RichTextUploadingField()
    to_person = ForeignKey(CustomUser, on_delete=RESTRICT)

    def __str__(self):
        return self.to_person.first_name


class Portfolio(Model):
    user = ForeignKey(CustomUser, on_delete=RESTRICT)
    name = CharField(max_length=255)
    image = ImageField(upload_to='user', default='default/default_post.jpg')
    url = CharField(max_length=255)

    def __str__(self):
        return self.name


class Contact(Model):
    name = CharField(max_length=255)
    email = EmailField(max_length=255)
    message = TextField()

    def __str__(self):
        return self.name


