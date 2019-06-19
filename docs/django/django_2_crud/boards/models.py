from django.db import models

# Create your models here.
class Board(models.Model):
    # id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=10)
    content = models.TextField()
    # auto_now_add : 생성일자 / DB 가 최초 저장시에만 적용
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}글 - {self.title}: {self.content}'

class Comment(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        # return self.content
        return f'<Board({self.board_id}): Comment({self.pk}-{self.content}>'
