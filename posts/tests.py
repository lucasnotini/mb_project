#import the TestCase module
from django.test import TestCase
#import our Post model
from .models import Post
#
from django.urls import reverse

# Create your tests here

#create a class to test our model Post
class PostModelTest(TestCase):
    #create a method to setup our database using the command .objects.create to POST the our string text into our table
    def setUp(self):
        Post.objects.create(text='just a post test')
    #create our first test function to test the text_content of the post
    def test_text_content(self):
        #retrive the post with id = 1
        post = Post.objects.get(id=1)
        #store the text of the post in a variable
        expected_object_name = f'{post.text}'
        #assert that our variable and the text we POSTED is equal
        self.assertEqual(expected_object_name, 'just a post test')

#create a class to test our homepage view
class HomePageViewTest(TestCase):
    #setUp create a fixture to prepare our test environment
    def setUp(self):
        Post.objects.create(text='this is another test')
    #create a function to test whether we get a 200 status code when visiting our home URL
    def test_view_url_exists_at_proper_location(self):
        #make a GET request to the URL '/'
        response = self.client.get('/')
        #assert that our response is equal to 200
        self.assertEqual(response.status_code, 200)
    #create a function to test if we can access a view by its name
    def test_view_url_by_name(self):
        #make a GET request to 'home'
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
    #create a test to check if the view uses the correct template    
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        #asserts that our response got the desired template
        self.assertTemplateUsed(response, 'home.html')