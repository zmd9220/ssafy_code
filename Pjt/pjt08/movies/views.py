from django.shortcuts import render, get_list_or_404, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Movie, Review, Comment
from .serializers import MovieSerializer, ReviewSerializer, CommentSerializer, ReviewListSerializer
from .tmdb import URLMaker
import requests
import pprint

@api_view(['GET'])
def movies(request):
    movie_list = get_list_or_404(Movie)
    serializer = MovieSerializer(movie_list, many=True)
    return Response(serializer.data)
    # if request.method =='POST':
    #     # 특정 값을 입력 받아서
    #     string = st
    #     if (st):
    #         urlmaker.make_url(string)
    #         dic = request.response(json)
    #         print(dic)

def search_movie(request, movie_title):
    # 특정 값을 입력 받아서
    # string = movie_title
    url_maker = URLMaker('031b6156fbe52ee9595fddf7b81190fa')
    url = url_maker.get_url(region='KR', language='ko')
    result = requests.get(url)
    if result:
        result_movie = result.json()
        result_list = result_movie['results']
        for rst in result_list:
            movie = Movie()
            movie.title = rst['title']
            movie.overview = rst['overview']
            movie.poster_path = rst['poster_path']
            movie.save()
        pprint.pprint(result_movie)

@api_view(['GET'])
def movie_detail(request, pk):
    movie = get_object_or_404(Movie,pk=pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def reviews(request, pk):
    movie = get_object_or_404(Movie,pk=pk)
    if request.method == 'GET':
        review_list = movie.review_set.all()
        serializer = ReviewListSerializer(review_list, many=True)
        return Response(serializer.data)
    else:
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie)
            return Response(serializer.data, status=201)

@api_view(['GET', 'PUT', 'DELETE'])
def review_detail(request, pk, review_pk):
    movie = get_object_or_404(Movie, pk=pk)
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie)
            return Response(serializer.data, status=201)
    else:
        review.delete()
        response = {'pk':pk}
        return Response(response, status=204)

            
@api_view(['GET', 'POST'])
def comments(request, pk, review_pk):
    # movie = get_object_or_404(Movie, pk=pk)
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'GET':
        comment_list = review.comment_set.all()
        serializer = CommentSerializer(comment_list, many=True)
        return Response(serializer.data)
    else:
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(review=review)
            return Response(serializer.data, status=201)
        