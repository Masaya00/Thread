from datetime import datetime
from tabnanny import verbose

from django.db import models


class Thread(models.Model):
    thread_name = models.CharField('スレッド名', max_length=32)
    created_at = models.DateTimeField('作成日時', default=datetime.now())
    del_flag = models.BooleanField('削除フラグ', default=False)

    class Meta:
        verbose_name = 'スレッド'
        verbose_name_plural = 'スレッド'

    def __str__(self) -> str:
        return self.thread_name


class Comment(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    content = models.CharField('コメント', max_length=255)
    created_at = models.DateTimeField('作成日時', default=datetime.now())

    class Meta:
        verbose_name = 'コメント'
        verbose_name_plural = 'コメント'

    def __str__(self) -> str:
        return self.content
