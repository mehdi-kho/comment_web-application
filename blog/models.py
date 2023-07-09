from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE,)
    body = models.TextField()

    def __str__(self):
        return self.title

    # def __str__(self):
    #     return "%s: [ ' %s ' , ' %s ' ] " % (self.author, self.title, self.body[:20])

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
