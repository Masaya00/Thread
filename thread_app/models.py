from datetime import datetime

from django.db import models


class Thread(models.Model):
    thread_name = models.CharField('スレッド名', max_length=32)
    created_at = models.DateTimeField('作成日時', default=datetime.now())

    def __str__(self) -> str:
        return self.thread_name


class Comment(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    content = models.CharField('コメント', max_length=255)
    created_at = models.DateTimeField('作成日時', default=datetime.now())

    def __str__(self) -> str:
        return self.content
