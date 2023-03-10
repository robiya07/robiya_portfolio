# Generated by Django 4.1.4 on 2022-12-27 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('image', models.ImageField(default='default/avatar.jpg', upload_to='user')),
                ('bio', models.TextField()),
                ('gender', models.CharField(max_length=255)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, max_length=255, null=True)),
                ('profession', models.CharField(max_length=255)),
                ('telegram', models.CharField(max_length=255)),
                ('instagram', models.CharField(max_length=255)),
                ('mail', models.CharField(max_length=255)),
                ('github', models.CharField(max_length=255)),
                ('service', models.ManyToManyField(to='apps.service')),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
