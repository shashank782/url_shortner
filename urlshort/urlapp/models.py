from django.db import models
from hashlib import md5
# Create your models here.
class Url(models.Model):
    F_url = models.CharField(unique=True,max_length=400)
    S_url= models.CharField(unique=True,max_length=20)


    def __str__(self):
        return self.F_url
    
    @classmethod
    def create(self, F_url):
        temp_url = md5(F_url.encode()).hexdigest()[:8]
        try:
            obj =self.objects.create(F_url=F_url, S_url= temp_url)
        except:
            obj = self.objects.get(F_url = F_url)
        return obj        

    


