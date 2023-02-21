from django.db import models
from common.models import CommonModel

#caption: 게시글 내용
#contentImg: 게시글 이미지
#likesNum: 좋아요 갯수
#reviewsNum: 댓글 갯수

#USER

class Feed(CommonModel):
    caption = models.CharField(max_length=1000,default="") #게시글내용
    contentImg = models.URLField(blank=True) #게시글이미지
    likesNum = models.PositiveBigIntegerField(default=0) #좋아요갯수
    reviewsNum = models.PositiveBigIntegerField(default=0) #댓글갯수