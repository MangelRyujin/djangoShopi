from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.

class PrincipalHeader(models.Model):
    principal_comment = models.CharField(_("Principal comment"),max_length=50)
    secundari_comment = models.CharField(_("Secundari comment"),max_length=100)
    link= models.URLField(_("Link"),null=True,blank=True)

    class Meta:
        verbose_name = _("Header")
        verbose_name_plural = _("Headers")

    def __str__(self):
        return self.principal_comment
    
class SocialMedia(models.Model):
    twitter= models.URLField(_("Twitter"),null=True,blank=True)
    instagram= models.URLField(_("Instagram"),null=True,blank=True)
    pinterest= models.URLField(_("Pinterest"),null=True,blank=True)
    gmail= models.URLField(_("Gmail"),null=True,blank=True)
    facebook= models.URLField(_("Facebook"),null=True,blank=True)
    tumblr= models.URLField(_("Tumblr"),null=True,blank=True)
    telegram= models.URLField(_("telegram"),null=True,blank=True)

    class Meta:
        verbose_name = _("SocialMedia")
        verbose_name_plural = _("SocialMedias")

    def __str__(self):
        return f'{self.id}'
    
class Brand(models.Model):
    brand_name = models.CharField(_("Brand name"),max_length=255)
    brand_image= models.ImageField(_("Brand image"),upload_to="brands_images")
    
    class Meta:
        verbose_name = _("Brand")
        verbose_name_plural = _("Brands")

    def __str__(self):
        return self.brand_name
    
class Contact(models.Model):
    contact_email= models.EmailField(_("Contact email"),max_length=255)
    
    class Meta:
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")

    def __str__(self):
        return self.contact_email


class AboutUs(models.Model):
    principal_title = models.CharField(_("Principal title"),max_length=50)
    principal_description = models.TextField(_("Principal description"),max_length=500)
    secundari_description = models.TextField(_("Secundari description"),max_length=500)
    

    class Meta:
        verbose_name = _("AboutUs")
        verbose_name_plural = _("AboutUs")

    def __str__(self):
        return self.principal_title
    
class FAQ(models.Model):
    title = models.CharField(_("Title"),max_length=100)
    description = models.TextField(_("Description"),max_length=500)
    

    class Meta:
        verbose_name = _("FAQ")
        verbose_name_plural = _("FAQ")

    def __str__(self):
        return self.title
    
class Step(models.Model):
    number= models.PositiveIntegerField(_("Step number"))
    title = models.CharField(_("Title"),max_length=100)
    description = models.TextField(_("Description"),max_length=500)
    
    class Meta:
        verbose_name = _("Step")
        verbose_name_plural = _("Steps")

    def __str__(self):
        return self.title
    
class Service(models.Model):
    name = models.CharField(_("Service name"),max_length=100)
    service_image= models.ImageField(_("Service image"),upload_to="services_images")
    description = models.TextField(_("Description"),max_length=500)
    
    class Meta:
        verbose_name = _("Service")
        verbose_name_plural = _("Services")

    def __str__(self):
        return self.name
    
class SiteReviews(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="site_reviews")
    rating = models.PositiveIntegerField(_("Rating"),validators=[MinValueValidator(1),MaxValueValidator(5)])
    create_date = models.DateField(_("Date"),auto_now_add=True)
    description = models.TextField(_("Description"),max_length=255)
    
    class Meta:
        verbose_name = _("Site Review")
        verbose_name_plural = _("Site Reviews")

    def __str__(self):
        return self.user.email