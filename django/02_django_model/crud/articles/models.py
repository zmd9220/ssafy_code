from django.db import models

# Create your models here.
# 게시글 관련 정보를 담는 모델이라고 가정
# 기본적으로 장고에서 어느정도의 틀을 제공해줌 그것을 상속- models.Model
# 모델 관리는 클래스로 관리
class Article(models.Model):
    # 스키마(데이터베이스 구조) 작성 - 설계도 작성
    # 모델필드?
    title = models.CharField(max_length=10)
    content = models.TextField()
    # 생성일자, 갱신일자는 우리가 일일히 지정하는것이아닌 서버가 당시마다 자동으로 갱신해줘야함
    # 처음 생성시에만(저장) 그 이후로 수정이 안됨
    created_at = models.DateTimeField(auto_now_add=True) 
    # 매번 저장 될때마다 값이 변경 (최종수정일)
    updated_at = models.DateTimeField(auto_now=True) 