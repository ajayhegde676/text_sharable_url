from django.core.signing import Signer
from rest_framework import permissions, status
from app.models import Text
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from app.serializers import TextSerializer,Text_Serializer
from rest_framework.authentication import TokenAuthentication


class TextView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'text_view.html'
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request,pk=None):
        mytext = get_object_or_404(Text,pk=pk).text_snippet
        q = Text.objects.get(text_snippet=mytext).text_snippet
        try:
            decrypted = Signer().unsign(q)
            return Response({'Texts': decrypted})
        except:
            return Response({'Texts': q})


class InputView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'input_view.html'

    def get(self, request):
        serializer = Text_Serializer()
        return Response({'serializer': serializer,'method':request.method})

    def post(self, request):
        serializer = TextSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if request.POST.get('encrypt') == 'on':
            serializer.save1()
            object_id = get_object_or_404(Text, text_snippet=Signer().sign(request.data['text_snippet'])).id
            queryset = Text.objects.get(id=object_id)
            return Response({'serializer': serializer, 'mytext': queryset, 'method': request.method})

        else:
            serializer.save()
            object_id = get_object_or_404(Text, text_snippet=request.data['text_snippet']).id
            queryset = Text.objects.get(id=object_id)
            return Response({'serializer': serializer, 'mytext': queryset, 'method': request.method})

