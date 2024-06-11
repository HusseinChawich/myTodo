from rest_framework import serializers
from .models import listItems

class listItemsSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=50, required=True)

    class Meta:
        model = listItems
        fields = ('__all__')
    
    def create(self, validated_data):
        return listItems.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)

        instance.save()
        return instance