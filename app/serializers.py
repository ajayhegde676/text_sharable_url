from django.core.signing import Signer
from rest_framework import serializers
from app.models import Text


class TextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Text
        fields = '__all__'

    def save1(self,**kwargs):
        signer = Signer()
        value = signer.sign(self.validated_data['text_snippet'])
        Text.objects.create(text_snippet=value).save()


class Text_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Text
        fields = '__all__'
