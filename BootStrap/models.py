from django.db import models

# Create your models here.
class CardMember(models.Model):
    identifier = models.IntegerField(primary_key=True,
                                     blank=False,
                                     null=False)
    nama = models.CharField(max_length=255)
    alamat = models.CharField(max_length=255)
    email = models.EmailField(blank=False, null=False)
    tempat_lahir = models.CharField(max_length=255)    
    tgl_lahir = models.DateField(null=True)
    phone = models.CharField(max_length=255,blank=True, null=True)
    # photo = models.ImageField()

    def __str__(self):
        return str(self.identifier) + " -- " +self.nama

    class Meta:
        verbose_name = "Smart Card Member Profile"