from django.db import models

# Create your models here.
class Board(models.Model):
    # id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=10)
    content = models.TextField()
    # auto_now_add : 생성일자 / DB 가 최초 저장시에만 적용
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
