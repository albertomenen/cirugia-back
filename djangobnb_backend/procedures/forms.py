from django.forms import ModelForm

from .models import Procedures

class ProcedureForm(ModelForm):
    class Meta:
        model = Procedures
        fields = (
            'title',
            'branddescription',
            'description',
            'price_per_procedure',
            'payment',
            'country',
            'country_code',
            'image',
        )
