from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import *
from rest_framework import mixins, generics
from rest_framework.viewsets import ViewSet, ModelViewSet
# Create your views here.

#modelview set.....urls router too
class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerailizer

#viewSet 
#changes in urls too ...routers
#course list + course detail
# class CourseViewSet(ViewSet):
#     def list(self, request):
#         courses = Course.objects.all()
#         serializer = CourseSerailizer(courses, many=True)
#         return Response(serializer.data)
    
#     def create(self,request):
#         serializer = CourseSerailizer(data =request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)
    
#     def retrieve(self, request, pk):
#         try:
#             course = Course.objects.get(pk=pk)
#         except Course.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         serializer = CourseSerailizer(course)
#         return Response(serializer.data)


#Generics
# class CourseListView(generics.ListCreateAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerailizer

# class CourseListView(generics.ListAPIView, generics.CreateAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerailizer

# class CourseDetailView(generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerailizer

#Mixins 
# class CourseListView(mixins.ListModelMixin, mixins.CreateModelMixin ,generics.GenericAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerailizer

#     def get(self, request):
#         return self.list(request)
    
#     def post(self, request):
#         return self.create(request)

# class CourseDetailView(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerailizer

#     def get(self, request, pk):
#         return self.retrieve(request, pk)

#     def put(self, request, pk):
#         return self.update(request, pk)

#     def delete(self, request, pk):
#         return self.destroy(request, pk)

#Class based View
# class CourseListView(APIView):
#     def get(self, request):
#         courses = Course.objects.all()
#         serializer = CourseSerailizer(courses, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         courseSerailizer = CourseSerailizer(data = request.data)
#         if courseSerailizer.is_valid():
#             courseSerailizer.save()
#             return Response(courseSerailizer.data, status=status.HTTP_201_CREATED)
#         return Response(courseSerailizer.errors)
    
# class CourseDetailView(APIView):

#     def get_course(self, pk):
#         try:
#             return Course.objects.get(pk=pk)
#         except Course.DoesNotExist:
#             raise Http404
#     def get(self, request, pk):
#         course = self.get_course(pk)
#         serializer = CourseSerailizer(course)
#         return Response(serializer.data)
    
#     def delete(self, request, pk):
#        self.get_course(pk).delete()
#        return Response(status=status.HTTP_204_NO_CONTENT)
       
    
#     def put(self, request, pk):
#         course = self.get_course(pk)
#         courseSerailizer = CourseSerailizer(course, data = request.data)
#         if courseSerailizer.is_valid():
#             courseSerailizer.save()
#             return Response(courseSerailizer.data)
#         return Response(courseSerailizer.errors)