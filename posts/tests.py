from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post

class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        #create a user
        testuser=User.objects.create_user(
            username='testuser',password='pwd123')
        testuser.save()
        #create a blog post 
        test_post=Post.objects.create(
            author=testuser,title='blog title', body='body content')
        test_post.save()


    def test_blog_content(self):
        post=Post.objects.get(id=1)
        author=f'{post.author}'
        title=f'{post.title}'
        body=f'{post.body}'
        self.assertEqual(author,'testuser')
        self.assertEqual(title,'blog title')
        self.assertEqual(body,'body content')