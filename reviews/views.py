from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from reviews.models import Review


# Create your views here.
class MyReviews(APIView):
    def get(self, request):
        # image this is the database
        reviews = []
        for review in Review.objects.filter() :
            reviews.append(review.review_text)
        return Response({'reviews' : reviews})
    

class StoreMyReviews(APIView):
    def post(self, request):
        review = request.data.get("review")
        database_add = Review(review_text=review)
        database_add.save()
        return Response({'message': 'success'})
