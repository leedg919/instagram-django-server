from django.db import models
from common.models import CommonModel

#caption: 댓글내용

#USER
#FEED
class Review(CommonModel):
    caption = models.CharField(max_length=150)
    
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        # user => review
        # user.review_set.all() -> user.reviews.all()
        related_name="reviews"
    )
    
    feed = models.ForeignKey(
        "feeds.Feed",
        on_delete=models.CASCADE,
        # feed => review
        # feed.reviews.all()
        related_name="reviews"
    )
