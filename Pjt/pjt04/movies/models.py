from django.db import models

# 영화 관련 db 설계도
class Movie(models.Model):
    # 제목
    title = models.CharField(max_length=100)
    # 줄거리
    overview = models.TextField()
    # 포스터 경로
    poster_path = models.CharField(max_length=500)