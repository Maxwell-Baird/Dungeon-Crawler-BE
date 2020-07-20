from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from dungeon.models import Encounter
from dungeon.serializers import DungeonSerializer
from rest_framework.decorators import api_view

@api_view(['GET', 'POST', 'DELETE'])
def encounter_list(request):
    if request.method == 'GET':
        encounters = Encounter.objects.all()
        encounters_serializer = DungeonSerializer(encounters, many=True)
        return JsonResponse(encounters_serializer.data, safe=False)

    elif request.method == 'POST':
        encounter_data = JSONParser().parse(request)
        encounter_serializer = DungeonSerializer(data=encounter_data)
        if encounter_serializer.is_valid():
            encounter_serializer.save()
            return JsonResponse(encounter_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(encounter_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        count = Encounter.objects.all().delete()
        return JsonResponse({'message': '{} Encounters were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'DELETE'])
def encounter_detail(request, pk):
    try:
        encounter = Encounter.objects.get(pk=pk)
    except Encounter.DoesNotExist:
        return JsonResponse({'message': 'The encounter does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        encounter_serializer = DungeonSerializer(encounter)
        return JsonResponse(encounter_serializer.data)

    elif request.method == 'DELETE':
        encounter.delete()
        return JsonResponse({'message': 'Encounter was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
