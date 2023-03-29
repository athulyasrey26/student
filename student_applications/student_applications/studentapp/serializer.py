from rest_framework import serializers
from .models import Application, Materials

class MaterialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materials
        fields = '__all__'

class ApplicationSerializer(serializers.ModelSerializer):
    materials = MaterialsSerializer(many=True)
    course_name = serializers.ReadOnlyField(source='course.name')
    department_name = serializers.ReadOnlyField(source='department.name')
    purpose_name = serializers.ReadOnlyField(source='purpose.name')
    class Meta:
        model = Application
        fields = '__all__'
