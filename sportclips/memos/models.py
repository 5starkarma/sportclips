from django.db import models
from django.urls import reverse
from django.utils import timezone
from users.models import User


class Memo(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_time = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('memos-detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    memo = models.ForeignKey(
        'memos.Memo',
        on_delete=models.CASCADE,
        related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def __str__(self):
        return self.text
