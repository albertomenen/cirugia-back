from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes


from .forms import ProcedureForm
from .models import Procedures
from .serializers import ProceduresListSerializer

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def procedures_list(request):
    procedures = Procedures.objects.all()
    serializer = ProceduresListSerializer(procedures, many=True)

    return JsonResponse({
        'data': serializer.data
    })

@api_view(['POST', 'FILES'])
def create_procedure(request):
    form = ProcedureForm(request.POST, request.FILES)

    if form.is_valid():         
        procedures = form.save(commit=False)
        procedures.landlord = request.user
        procedures.save()

        return JsonResponse({'success': True})
    else:
        print('error', form.errors, form.non_field_errors)
        return JsonResponse({'errors':form.errors.as_json()}, status=400)
    