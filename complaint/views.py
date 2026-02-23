from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Complaint
from .serializers import ComplaintSerializer
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator


@api_view(['GET','POST'])
@cache_page(60)
@permission_classes([IsAuthenticated])
def complaint_list(request):
    if request.method == 'GET':

        complaints = Complaint.objects.all()
        category = request.query_params.get('category')
        priority = request.query_params.get('priority')
        status_param = request.query_params.get('status')

        if category:
            complaints = complaints.filter(category=category)
        if priority:
            complaints = complaints.filter(priority=priority)
        if status_param:
            complaints = complaints.filter(status=status_param)

        ordering = request.query_params.get('ordering')
        if ordering:
            complaints = complaints.order_by(ordering)


        #pagination
        paginator = PageNumberPagination()
        paginator.page_size = 3

        paginated_complaints = paginator.paginate_queryset(complaints, request)
        serializer = ComplaintSerializer(paginated_complaints, many=True)

        return paginator.get_paginated_response(serializer.data)
    
    if request.method == 'POST':
        serializer = ComplaintSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET','PUT','DELETE','PATCH'])
@permission_classes([IsAuthenticated])
@cache_page(60)
def complaint_detail(request,id):
    try:
        complaint = Complaint.objects.get(id=id)
    except Complaint.DoesNotExist:
        return Response({'error':'Not Found'}, status=404)
    if request.method == 'GET':
        serializer = ComplaintSerializer(complaint)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = ComplaintSerializer(complaint, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    if request.method == 'DELETE':
        complaint.delete()
        return Response({'message':'deleted'})
    
    if request.method == 'PATCH':
        serializer = ComplaintSerializer(complaint, data=request.data,partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)