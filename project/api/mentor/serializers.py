from rest_framework import serializers

from apps.mentor.models import Mentor


class MentorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        fields = '__all__'