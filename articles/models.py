from django.db import models
from django.urls import reverse

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=200) #CharField는 단문 텍스트
    content = models.TextField() #TextFiled는 장문 텍스트
    author = models.ForeignKey( #외부에서 가져오는 데이터면 ForeignKey
        "auth.User",
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.author} - {self.title}" #self는 만들어진 instance이고 title를 나타낸다.

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"pk": self.pk}) #primary key 각 상품별 위치 값
        
    

