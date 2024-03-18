import uuid

from django.conf import settings
from django.db import models

from useraccount.models import User

class Procedures(models.Model):
        id= models.UUIDField(primary_key=True, default=uuid.uuid4, editable= False)
        title = models.CharField(max_length=255)
        description = models.TextField()
        branddescription = models.TextField()
        price_per_procedure = models.IntegerField()
        days_procedure= models.IntegerField()
        size_cc= models.IntegerField()
        hospitals=models.TextField(max_length=50)
        information_procedure=models.TextField()
        payment= models.TextField()
        country = models.CharField(max_length=255)
        country_code= models.CharField(max_length=10)
        category = models.CharField(max_length=255)

        #favorited

        image=models.ImageField(upload_to='uploads/procedures')
        doctor = models.ForeignKey(User, related_name='procedures', on_delete=models.CASCADE)
        created_at = models.DateTimeField(auto_now_add=True)
        
        def image_url(self):
                return f'{settings.WEBSITE_URL}{self.image.url}'
