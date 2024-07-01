from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from utils.validators.validations import validate_phone_number
from django.db.models.signals import post_save
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name="profile")
    image = models.ImageField(_("Image"),upload_to="users_images",null=True,blank=True)
    phone_number = models.CharField(_("Phone number"),max_length=20, validators=[validate_phone_number],null=True,blank=True)
    country = models.CharField(_("Country"), max_length=255,null=True,blank=True)
    city = models.CharField(_("Country"),max_length=255, null=True,blank=True)
    address = models.CharField(_("Address"),max_length=255, null=True,blank=True)

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")

    def __str__(self):
        return self.user.username

    
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
        
        
def save_user_profile(sender,instance,**kwargs):
    instance.profile.save()
    
post_save.connect(create_user_profile,sender=User)
post_save.connect(save_user_profile,sender=User)