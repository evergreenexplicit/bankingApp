from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
class BankUser(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        default=""
    )
    money = models.PositiveIntegerField(default=500)

@receiver(post_save, sender=User)
def create_user_account(sender, instance, created, **kwargs):
    if created:
        BankUser.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_account(sender, instance, **kwargs):
    instance.bankuser.save()

class Transaction(models.Model):
    sender = models.ForeignKey(BankUser, on_delete=models.CASCADE,related_name='sender')
    receiver = models.ForeignKey(BankUser, on_delete=models.CASCADE,related_name='receiver')
    moneyValue = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def save(self,*args,**kwargs):
        self.sender.money-=self.moneyValue
        self.receiver.money+=self.moneyValue
        self.sender.save()
        self.receiver.save()
        super().save(*args,**kwargs)

# Create your models here.
