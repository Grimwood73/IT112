from turtle import title
from django.test import TestCase
from .models import Meeting, MeetingMinutes, Resource, Event
from django.contrib.auth.models import User
import datetime
from django.urls import reverse_lazy, reverse

class MeetingTest(TestCase):
    def setUp(self):
        self.type=Meeting(meetingtitle='TestMeeting')

    def test_typestring(self):
        self.assertEqual(str(self.type), 'TestMeeting')
    
    def test_tablename(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')

class ResourceTest(TestCase):
    def setUp(self):
        self.type=Resource(resourcename='TestResource')

    def test_typestring(self):
        self.assertEqual(str(self.type), 'TestResource')
    
    def test_tablename(self):
        self.assertEqual(str(Resource._meta.db_table), 'resource')

class EventTest(TestCase):
    def setUp(self):
        self.type=Event(eventtitle='TestEvent')

    def test_typestring(self):
        self.assertEqual(str(self.type), 'TestEvent')
    
    def test_tablename(self):
        self.assertEqual(str(Event._meta.db_table), 'event')

class New_Resource_Authentication_Test(TestCase):
    def setUp(self):
        self.test_user=User.objects.create_user(username='testuser1', password='P@ssw0rd1')
        self.resource=Resource.objects.create(resourcename='test_resource', 
        resourcetype='website', url='http://www.butts.com', dateentered=datetime.date(2021,1,10),
        userid=self.test_user, description='testdescription')

    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('newresource'))
        self.assertRedirects(response, '/accounts/login/?next=/club/newresource/')


