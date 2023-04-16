from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers

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