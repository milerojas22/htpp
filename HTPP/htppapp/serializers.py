from .models import PersonMonoku
from rest_framework import serializers


class PersonaMonokuSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PersonMonoku
        fields = ('id', 'name_person', 'email_person', 'age_person')