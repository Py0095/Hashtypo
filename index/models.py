from django.db import models
from django.utils import timezone
from django.utils.text import slugify

# Create your models here.

class Atik(models.Model):
    email=models.CharField(max_length=45,blank=True,null=True)
    slug=models.SlugField(unique=True,max_length=50)
    tit=models.CharField(max_length=50)
    Ote=models.CharField(max_length=100,default='')
    kontni=models.TextField(max_length=5000)
    dat_piblikasyon=models.DateField(default=timezone.now)
    publik = models.BooleanField(default=False)
    total_vizit = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.tit
    class Meta:
        verbose_name='Atik la'
        verbose_name_plural='Atik yo'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.tit)
        super(Atik, self).save(*args, **kwargs)
