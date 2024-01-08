from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ItemSerialier
from .models import Item
# Create your views here.

@api_view(['GET', 'POST'])
def items(request):
    if request.method == 'GET':
        items = Item.objects.all()
        serializer = ItemSerialier(items, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ItemSerialier(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def remove_item(request, id):
    try:
        instance = Item.objects.get(id=id)
        instance_id = id
        instance.delete()
        return Response({'message': f'Resource with ID {instance_id} deleted successfully'}, status=status.HTTP_204_NO_CONTENT)        
    except Item.DoesNotExist:
        return Response({'error': 'Resource not found'}, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['PUT'])
def update_item(request, id):
    try:
        instance = Item.objects.get(id=id)
        instance_id = id
        serializer = ItemSerialier(instance, data=request.data)
        if serializer.is_valid():
            instance.name = serializer.validated_data.get('name', instance.name)
            instance.save()
            return Response({'message': f'Resource with ID {instance_id} updated successfully'})
    except Item.DoesNotExist:
        return Response({'error': 'Resource not found'}, status=status.HTTP_404_NOT_FOUND)