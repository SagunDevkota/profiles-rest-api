from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
from rest_framework import viewsets

class HelloApiView(APIView):
    """Test API View"""
    serializers_class = serializers.HelloSerilizer


    def get(self, request, format=None): # for HTTP GET request
        """Return a list of API view features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
    

    def post(self,request):
        """Create a hello message with our name"""
        serializers = self.serializers_class(data=request.data)

        if(serializers.is_valid()):
            name = serializers.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        
    
    def put(self,request,pk = None):
        """Handle updating an existing object"""
        return Response({'method': 'PUT'})
    
    
    def patch(self,request,pk = None):
        """Handle a partial update of an object"""
        return Response({'method': 'PATCH'})
    

    def delete(self,request,pk = None):
        """Delete an object"""
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test API viewset"""

    searilizer_class = serializers.HelloSerilizer

    def list(self,request):
        """Return a hello message"""
        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code',
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})
    

    def create(self, request):
        """Create a new hello message"""
        serializer = self.searilizer_class(data=request.data)

        if(serializer.is_valid()):
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

    def retrieve(self, request,pk=None):
        """Handle getting an object by it's id"""
        return Response({"http_method":"GET"})
    

    def update(self,request,pk=None):
        """Handle updating an object"""
        return Response({"http_method":"PUT"})
    

    def destroy(self,request,pk=None):
        """Handle deleting an object"""
        return Response({"http_method":"DELETE"})
    

    def partial_update(self,request,pk=None):
        """Handle partial updating an object"""
        return Response({"http_method":"PATCH"})