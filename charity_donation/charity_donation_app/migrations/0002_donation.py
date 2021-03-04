# Generated by Django 3.1.7 on 2021-03-04 13:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('charity_donation_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('address', models.CharField(max_length=64)),
                ('phone_number', models.IntegerField()),
                ('city', models.CharField(max_length=64)),
                ('zip_code', models.CharField(max_length=16)),
                ('pick_up_date', models.DateField()),
                ('pick_uP_time', models.TimeField()),
                ('pick_up_comment', models.TextField()),
                ('categories', models.ManyToManyField(to='charity_donation_app.Category')),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='charity_donation_app.institution')),
                ('user', models.ForeignKey(default='Null', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
