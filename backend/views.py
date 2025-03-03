from django.shortcuts import render
from .models import Article
from .serializers import ArticleSerializer
from rest_framework.parsers import JSONParser
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework .views import APIView
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthor

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'slug'
    # authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated, IsAuthor]

    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    
    def list(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    
    
    def create(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
          
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
 
'''
class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'slug'
'''    

'''
class ArticleList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ArticleDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'slug'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    '''
# class ArticleList(APIView):
#     def get(self, request):
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class ArticleDetail(APIView):
#     def get_object(self, slug):
#         try:
#             return Article.objects.get(slug=slug)
#         except Article.DoesNotExist:
#             return None
    
#     def get(self, request, slug):
#         article = self.get_object(slug)
#         if article is None:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)
    
#     def put(self, request, slug):
#         article = self.get_object(slug)
#         if article is None:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, slug):
#         article = self.get_object(slug)
#         if article is None:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#     def get(self, request):
#         articles =Article.objects,all()

# @api_view(['GET','POST'])
# def article_list(request):
#     if request.method == 'GET':
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)
    
#     elif request.method == 'POST':
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET','PUT','DELETE'])
# def article_details(request, slug):
#     try:
#         article = Article.objects.get(slug=slug)
#     except Article.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'GET':
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)
    
#     elif request.method == 'PUT':
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     elif request.method == 'DELETE':
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
# # @csrf_exempt
# # def article_list(request):
# #     # get all articles
# #     if request.method == "GET":
# #         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)  
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == "POST":
#         data = JSONParser().parse(request)
#         serializer = ArticleSerializer(data=data)
        
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)  
    
# @csrf_exempt
# def article_details(request, slug):
#     try:
#         article = Article.objects.get(slug=slug)
#     except Article.DoesNotExist:
#         return HttpResponse(status=404)
    
#     if request.method == "GET":
#         serializer = ArticleSerializer(article)
#         return JsonResponse(serializer.data)
    
#     elif request.method == "PUT":
#         data = JSONParser().parse(request)
#         serializer = ArticleSerializer(article, data=data)

#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)
    
#     elif request.method == "DELETE":
#         article.delete()
#         return HttpResponse(status=204)