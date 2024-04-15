from sre_constants import SUCCESS
from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes


from .forms import ProcedureForm
from .models import Procedures, Reservation
from .serializers import ProceduresListSerializer
from .serializers import ProcedureDetailSerializer, ProcedureDetailSerializer, ReservationsListSerializer

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def procedures_list(request):
    procedures = Procedures.objects.all()
    

    # Filter

    doctor_id = request.GET.get('doctor_id')

    if doctor_id:
        procedures = procedures.filter(doctor_id=doctor_id)

    

    serializer = ProceduresListSerializer(procedures, many=True)

    return JsonResponse({
        'data': serializer.data
    })

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def procedure_detail(request, pk):
    procedures= Procedures.objects.get(pk=pk)

    serializer = ProcedureDetailSerializer(procedures, many=False)

    return JsonResponse(serializer.data)

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def procedure_reservation(request, pk):
    procedures= Procedures.objects.get(pk=pk)
    reservations = procedures.reservations.all()

    serializer = ReservationsListSerializer(reservations, many=True)

    return JsonResponse(serializer.data, safe=False)


@api_view(['POST', 'FILES'])
def create_procedure(request):
    form = ProcedureForm(request.POST, request.FILES)

    if form.is_valid():         
        procedures = form.save(commit=False)
        procedures.doctor = request.user
        procedures.save()

        return JsonResponse({'success': True})
    else:
        print('error', form.errors, form.non_field_errors)
        return JsonResponse({'errors':form.errors.as_json()}, status=400)
    

@api_view(['POST'])
def book_procedure(request, pk):
    try:
        start_date = request.POST.get('start_date', '')
        end_date = request.POST.get('end_date', '')
        total_price = request.POST.get('total_price', '')
        guests = request.POST.get('guests', '')

        procedures=Procedures.objects.get(pk=pk)

        Reservation.objects.create(
            procedures=procedures,
            start_date=start_date,
            end_date=end_date,
            total_price=total_price,
            guests=guests,
            created_by=request.user
        )

        return JsonResponse({'success': True})

    except Exception as e:
        print('Error', e)

        return JsonResponse({'success': False})
    