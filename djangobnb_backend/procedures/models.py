import uuid

from django.conf import settings
from django.db import models

from useraccount.models import User

class Procedures(models.Model):
        id= models.UUIDField(primary_key=True, default=uuid.uuid4, editable= False)
        title = models.CharField(max_length=255)
        description = models.TextField()
        price_per_procedure = models.IntegerField()
        hospitals=models.TextField(max_length=50)
        information_procedure=models.TextField()
        guests = models.IntegerField()
        payment= models.TextField(null=True)
        country = models.CharField(max_length=255)
        country_code= models.CharField(max_length=10)
        category = models.CharField(max_length=255)

        favorited = models.ManyToManyField(User, related_name='favorites', blank=True)

        image=models.ImageField(upload_to='uploads/procedures')
        doctor = models.ForeignKey(User, related_name='procedures', on_delete=models.CASCADE)
        created_at = models.DateTimeField(auto_now_add=True)
        
        def image_url(self):
                return f'{settings.WEBSITE_URL}{self.image.url}'
        

class Reservation (models.Model):
        id= models.UUIDField(primary_key=True, default=uuid.uuid4, editable= False)
        procedure= models.ForeignKey(Procedures, related_name='reservations', on_delete=models.CASCADE)
        start_date= models.DateField()
        end_date= models.DateField()
        total_price = models.FloatField()
        # Vamos a cambiar el de guest por type of process
        guests = models.IntegerField()
        created_by = models.ForeignKey(User, related_name='reservations', on_delete=models.CASCADE)
        created_at= models.DateField(auto_now_add= True)


