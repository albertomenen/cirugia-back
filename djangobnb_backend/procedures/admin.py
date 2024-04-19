from django.contrib import admin


from .models import Procedures, Reservation


admin.site.register(Procedures)

admin.site.register(Reservation)