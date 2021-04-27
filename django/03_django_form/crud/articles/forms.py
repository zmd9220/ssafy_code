# Django의 주요 유효성 검사 도구 중 하나
# 공격이나 우연한 데이터 손상에 대한 방어 수단.

from django import forms
from .models import Article

# 두가지 기능
# 1. 입력 받을 공간을 생성 해주는 기능 = 자동 form 생성 기능 = Markup input을 생성하는 기능
# (기존에는 html문서로 직접 입력공간을 생성해줬다면 장고는 forms가 생성해줌)
# 그러면 html 문서가 간결해져서 좋음
# 생성시 부터 유효성에 맞게 form을 자동생성(max_length=20, required 이런거)
# 2. 사용자가 입력한 데이터를 받아서 유효성 검사(validation)
# class ArticleForm(forms.Form):
#     # 사용자에게 입력 받을 필드
#     # max_length가 필수가 아님 있으면 해당 범위까지만 있는지 체크
#     title = forms.CharField(max_length=20) 
#     # textfield가 없음 (문자로 받을거야)
#     # widget=forms.Textarea 처럼 인풋 타입 양식을 정해줄 수 있음
#     content = forms.CharField(widget=forms.Textarea) 
#     # 생성시간, 갱신시간은 사용자로 부터 입력받는 데이터가 아니기 때문에 안넣어도 됨


# form의 속성 들을 보면 대부분 model의 속성과 일맥상통하기 때문에 장고에선 모델과 바로 연결해줘서 쉽게 form을 생성하게 하는 기능이 존재
# 이렇게 안하면 폼에도 항상 속성에 맞춰 일일히 연결해야함 - 왜냐면 서로간의 연결이 없기 때문에 모델과 유사하게 속성을 가진 폼을 개인적으로 생성해야하기 때문
class ArticleForm(forms.ModelForm):
    # title 속성 꾸미기
    title = forms.CharField(
        # 라벨(사용자가 보는 속성 명)
        label='제목',
        # 실제 데이터 넣는 공간쪽(인풋 텍스트) 속성 추가~?
        widget=forms.TextInput(
            attrs={
                # 딕셔너리
                'class': 'my-title',
                'placeholder': 'Enter title',
                # 직접 위젯을 만들때는 기본 속성들이 적용안되므로(오버라이딩과 비슷) 직접 넣어줘야함(여기서는 최대길이 20자가)
                'maxlength': 20,
            }
        )
    )
    # content
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'my-content',
                'placeholder': 'Enter content',
                'rows': 5,
                'cols': 50,
            }
        )
        error_messages={
            'required': 'Please enter your content',
        }
    )

    # 메타 데이터
    # 데이터에 대한 데이터?
    # 데이터를 설명하기 위한 데이터
    # ex - 사진 파일에서 파일 이름, 찍은 일자, 파일 크기, 사진 크기, 파일 위치, 등등
    # form에선 그 설명에 해당하는 부분을 Meta 클래스에서 생성
    class Meta:
        # 어떤 모델을 쓸 것인지? 즉 해당 모델과 이 클래스간의 연결 
        # 그래서 필드들을 작성하지 않아도 모델을 통해 속성들이 무엇인지 알게 되므로 장고가 자동으로 해당하는 속성들을 인식함
        model = Article
        # 어떤 필드를 사용 할 것인지? __all__ 모든 필드 사용
        fields = '__all__' 