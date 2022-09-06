from concurrent.futures import thread
from django.test import TestCase
from thread_app.models import Thread, Comment

class ThreadModelTests(TestCase):
    """スレッドモデルのテスト"""
    def test_is_empty(self):
        """初期状態では何も登録されていないことをチェック"""
        thread = Thread.objects.all()
        self.assertEqual(thread.count(), 0)

    def test_is_create(self):
        """スレッドが正常に作成されることをチェック"""
        Thread.objects.create(thread_name="テストスレッド")
        thread = Thread.objects.last()
        self.assertEqual(thread.thread_name, 'テストスレッド')


class CommentModelTest(TestCase):
    """コメントモデルのテスト"""
    def test_is_empty(self):
        comment = Comment.objects.all()
        self.assertEqual(comment.count(), 0)

    def test_is_create(self):
        """コメントが正常に作成されることをチェック"""
        Thread.objects.create(thread_name="テストスレッド")
        thread = Thread.objects.all().last()
        Comment.objects.create(thread=thread, content="テストコメント")
        comment = Comment.objects.last()
        self.assertEqual(comment.content, 'テストコメント')

