from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from .models import *
from .serializers import ArticleSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

# Create your views here.


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication,]



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer




# class ArticleView(APIView):
#     permission_classes = [IsAuthenticated]
#     authentication_classes = [TokenAuthentication,]

#     def get(self,request):
#         articles = Article.objects.all()
#         serializers = ArticleSerializer(articles,many=True)
#         return Response(serializers.data)

# class ArticleDetailView(APIView):
#     permission_classes = [IsAuthenticated]
#     authentication_classes = [TokenAuthentication,]

#     def get(self,request,pk):
#         article = Article.objects.get(id=pk)
#         serializers = ArticleSerializer(article,many=False)
#         return Response(serializers.data)

# class ArticleCreateView(APIView):
#     permission_classes = [IsAuthenticated]
#     authentication_classes = [TokenAuthentication,]

#     def post(self,request):
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
        



# class ArticleUpdateView(APIView):
#     permission_classes = [IsAuthenticated]
#     authentication_classes = [TokenAuthentication,]

#     def put(self,request,pk):
#         article = Article.objects.get(id=pk)
#         serializer = ArticleSerializer(article,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)


# class ArticleDeleteView(APIView):
#     permission_classes = [IsAuthenticated]
#     authentication_classes = [TokenAuthentication,]

#     def delete(self,request,pk):
#         article = Article.objects.get(id=pk)
#         article.delete()
#         return Response('Article Deleted Successfully')


