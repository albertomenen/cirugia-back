from sre_constants import SUCCESS
from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework_simplejwt.tokens import AccessToken

from .forms import ProcedureForm
from .models import Procedures, Reservation
from .serializers import ProceduresListSerializer
from .serializers import ProcedureDetailSerializer, ProcedureDetailSerializer, ReservationsListSerializer
from useraccount.models import User

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def procedures_list(request):
    # Auth

    try:
        token= request.META['HTTP_AUTHORIZATION'].split('Bearer')[1]
        token=AccessToken(token)
        user_id= token.payload['user_id']
        user= User.objects.get(pk=user_id)

    except Exception as e:
        user= None

    print('user', user)
    ##


    favorites = []
    procedures = Procedures.objects.all()
    

    # Filter
    is_favorites= request.GET.get('is_favorites', '')
    doctor_id = request.GET.get('doctor_id')

    if doctor_id:
        procedures = procedures.filter(doctor_id=doctor_id)

    if is_favorites:
        procedures = procedures.filter(favorited__in=[user])

    ## Favorites

    if user:
        for procedure in procedures:
            if user in procedure.favorited.all():
                favorites.append(procedure.id)

    

    serializer = ProceduresListSerializer(procedures, many=True)

    return JsonResponse({
        'data': serializer.data,
        'favorites': favorites
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
    procedure= Procedures.objects.get(pk=pk)
    reservations = procedure.reservations.all()

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
            procedure=procedures,
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
    
@api_view(['POST'])
def toggle_favorite(request,pk):
     
     procedures=Procedures.objects.get(pk=pk)

     if request.user in procedures.favorited.all():
         procedures.favorited.remove(request.user)

         return JsonResponse ({'is_favorited': False})
     else:
         procedures.favorited.add(request.user)

         return JsonResponse ({'is_favorited': True})
         

    