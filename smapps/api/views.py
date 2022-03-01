from email.policy import HTTP
from django.shortcuts import get_object_or_404
from .serializers import *
from ..models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
import json
from rest_framework.status import *
from rest_framework.response import Response
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse

class PostView(APIView):   
    permission_classes = [IsAuthenticated]    
    def get(self,request):
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many = True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
            serializer = PostSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response("Data_Created", status=status.HTTP_200_OK)

    def delete(self, request, pk, format=None):
        id = pk
        post = Post.objects.get(pk=id)
        post.delete()
        return Response({'msg':'Data Deleted'})

    
class TokenView(APIView):
     permission_classes = [IsAuthenticated]
     def get(self ,request):
         print(request.user)
         return Response({'sucess' : "I am Ready to authenticated"})
    
class ProfileView(APIView):

    def get(self,request):
        queryset = Profile.objects.all()
        serializer = ProfileSerializer(queryset, many = True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
            serializer = ProfileSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response("Data_Created", status=status.HTTP_200_OK)

    def delete(self, request, pk, format=None):
        id = pk
        profile = Profile.objects.get(pk=id)
        profile.delete()
        return Response({'msg':'Data Deleted'})

class LikeView(APIView):     
    permission_classes=[IsAuthenticated,]
   
    def get(self,request): 
        queryset = Like.objects.all()
        serializer = LikeSerializer(queryset, many = True)
        return Response(serializer.data)

    def post(self,request,*args,**kwargs):
        user = request.user
        id=request.data.get('id')
        try:
            post = Post.objects.get(id=id)
        except:
            return Response({
                'success' : 'False',
                'message' : 'post Not found',})
        liked= False
        like = Like.objects.filter(user=user,post=post)
        if like:
            like.delete()
        else:
            liked = True
            Like.objects.create(user=user,post=post)            
        resp =Like.objects.filter(post=post).count()      
        return Response({'like':resp}, status=HTTP_200_OK)    
    
class CommentView(APIView): 
    permission_classes=(IsAuthenticated,)
    def post(self,request,*args,**kwargs):
        user = request.user
        # feedback=request.data.get('feedback')
        id=request.data.get('id')
        try:
            post = Post.objects.get(id=id)
        except:
            return Response({
                'success' : 'False',
                'message' : 'No post found',
            },status=HTTP_400_BAD_REQUEST)
        
        Comments.objects.create(user=user,post=post)
            
        resp = {
            'count':Comments.objects.filter(post=post).count()
        }
        count=Like.objects.all().count()
        response = json.dumps(resp)
        return HttpResponse(response, content_type = "application/json")
       
    
class Send_FriendRequest(APIView):
    permission_classes=(IsAuthenticated,)
    # def send_friend_request(request, userID):
    #     from_user = request.user
    #     to_user = User.objects.get(id=userID)
    #     friend_request, created = Friends.objects.get_or_create(from_user=from_user,to_user=to_user)
    #     if created:
    #         return HttpResponse('friend request sent')
    #     else:
    #         return HttpResponse('friend request was already sent')

    def post(self, request, format=None):
            serializer = Friend_requestSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response("friend request sent", status=status.HTTP_200_OK)


# class Accept_FriendRequest(APIView):
#     permission_classes=(IsAuthenticated,)
#     def accept_friend_request(request, requestID):
#         friend_request = Friends.objects.get(id=requestID)
#         if friend_request.to_user == request.user:
#             friend_request.to_user.friends.add(friend_request.from_user)
#             friend_request.from_user.friends.add(friend_request.to_user)            
#             friend_request.delete()
#             return HttpResponse('friend request accept')
#         else:
#             return HttpResponse('friend request was not accept')






