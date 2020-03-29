# serializers for the models
from rest_framework import serializers
from lead_manager.models import Leads
from django.shortcuts import get_object_or_404

class LeadsSerializer(serializers.ModelSerializer):
    class Meta:
        model= Leads
        fields = ('id','first_name', 'last_name',
        'email', 'contacted', 'notes', 'created_At', "updated_At")

    def create(self, validated_data):
        print("CREATE VALID DATA", validated_data)
        instance = Leads.objects.create(**validated_data)
        return instance
    
    def update(self, instance, validated_data):
        instance_id = instance.id
        if "email" in validated_data.keys():
            instance.email = validated_data["email"]
        if "contacted" in validated_data.keys():
            instance.contacted = validated_data["contacted"]
        if "notes" in validated_data.keys():
            instance.notes = validated_data["notes"]
        if "first_name" in validated_data.keys():
            instance.first_name = validated_data["first_name"]
        if "last_name" in validated_data.keys():
            instance.last_name = validated_data["last_name"]
        
        instance.save()
        
        # instance.update(**validated_data)
        return instance