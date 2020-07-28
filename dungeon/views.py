from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from dungeon.models import Npc
from dungeon.serializers import NpcSerializer
from rest_framework.decorators import api_view

@api_view(['GET', 'POST', 'DELETE'])
def npc_list(request):
    if request.method == 'GET':
        npcs = Npc.objects.all()

        npc_serializer = NpcSerializer(npcs, many=True)
        return JsonResponse(npc_serializer.data, safe=False)

    elif request.method == 'POST':
        npc_data = JSONParser().parse(request)
        npc_serializer = NpcSerializer(data=npc_data)
        if npc_serializer.is_valid():
            npc_serializer.save()
            return JsonResponse(npc_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(npc_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        count = Npc.objects.all().delete()
        return JsonResponse({'message': '{} NPCS were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def npc_detail(request, pk):

    try:
        npc = Npc.objects.get(pk=pk)
    except Npc.DoesNotExist:
        return JsonResponse({'message': 'The npc does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        npc_serializer = NpcSerializer(npc)
        return JsonResponse(npc_serializer.data)
    elif request.method == 'PUT':
        npc_data = JSONParser().parse(request)
        npc_serializer = NpcSerializer(npc, data=npc_data)
        if npc_serializer.is_valid():
            npc_serializer.save()
            return JsonResponse(npc_serializer.data, status=status.HTTP_202_ACCEPTED)
        return JsonResponse(npc_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        npc.delete()
        return JsonResponse({'message': 'NPC was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
