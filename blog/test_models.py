from django.test import TestCase
from django.contrib.auth.models import User
from .models import Blog
from forum.models import Topic


class TestBlog(TestCase):
    
    # Test User
    def setUp(self):
        self.user = User.objects.create_user(
                username="test_username",
                password="test_password"
            )
            
    def test_create_blog(self):
        
        self.client.force_login(self.user)
        
        # Test create blog post 
        blog = Blog(
            title = "test_title",
            topic = "test_topic",
            description = "test_description",
            author = self.user,
            image = "test_image"
        )
        blog.save()
        
        self.assertTrue(blog.date)
        self.assertEqual(blog.title, "test_title")
        self.assertEqual(blog.author.username, "test_username")
        
        # Test to check save() creates a Topic with same data
        topic = Topic.objects.get(id=blog.forum_id.id)
        
        self.assertEqual(topic.title, "test_title")