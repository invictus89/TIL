from django.db import models
from django.conf import settings
 # model이 아닌 곳에서 user 를 가져오려면 get_user를 사용한다.

# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # settings ~ : 스트링, model 은 insetalled_app 보다 먼저 실행된다. 따라서 아래 함수를 사용하면 인식을 못한다.
    # get_user_model() : 함수이다.
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_boards', blank=True)
    
    class Meta:
        ordering = ('-pk',)

    def __str__(self):
        return self.title
    
