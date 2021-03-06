# Generated by Django 2.2.7 on 2019-11-17 23:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('logins', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bankuser',
            name='id',
        ),
        migrations.RemoveField(
            model_name='bankuser',
            name='monies',
        ),
        migrations.RemoveField(
            model_name='bankuser',
            name='username',
        ),
        migrations.AddField(
            model_name='bankuser',
            name='money',
            field=models.IntegerField(default=500),
        ),
        migrations.AddField(
            model_name='bankuser',
            name='user',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.PositiveIntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to='logins.BankUser')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='logins.BankUser')),
            ],
        ),
    ]
