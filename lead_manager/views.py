from graphene_django.views import GraphQLView
from django.shortcuts import render
from lead_manager.models import Leads
from lead_manager.serializers import LeadsSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, get_list_or_404
# Create your views here.

class getLeads(viewsets.ModelViewSet):
    ''' The actions provided by the ModelViewSet class are .list(), .retrieve(),
      .create(), .update(), .partial_update(), and .destroy(). '''
    
    queryset = Leads.objects.all()
    serializer_class = LeadsSerializer
    # lookup_field = 'email'
    lookup_value_regex = '[\w@.]+'

    print("ENTER API")
    def list(self, request):
        # accessed at url ^api/v1/leads/$
        print("LIST")
        queryset = Leads.objects.all()
        serializer = LeadsSerializer(queryset, many=True)

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        # accessed at url: ^api/v1/leads/{pk}/$
        print("RETRIEVE", pk)
        queryset = Leads.objects.all()
        records = get_list_or_404(queryset, email__exact=pk)
        serializer = LeadsSerializer(records, many=True)

        return Response(serializer.data)
    
    def update(self, request, pk=None):
        
        queryset = Leads.objects.all()
        instance = get_object_or_404(queryset, email__exact=pk)
        serializer = LeadsSerializer(instance, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        queryset = Leads.objects.all()
        print("DELETE", pk)
        user_info = []
        instance = queryset.get(email=pk)
        instance.delete()
        return Response("Deleted user", status=status.HTTP_200_OK)
        