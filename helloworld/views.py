from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from helloworld.serializers import *
from rest_framework.permissions import IsAuthenticated

class HomeView():
	@api_view(['GET'])
	def hi(request):
		return Response({'status': 'OK', 
			'message': 'Hello ' + request.query_params.get('name', 'world')}, 200)

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = (IsAuthenticated,)