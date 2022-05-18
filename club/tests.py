from turtle import title
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Meeting, MeetingMinutes, Resource, Event
import datetime


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

#class MeetingMinutes(TestCase):
    #def setUp(self):
            #self.type=Meeting(meetingtitle='TestMeeting')
            #self.meetingminutes=MeetingMinutes(meetingid=self.type)

    #def test_typestring(self):
        #self.assertEqual(str(meetingminutes), 'TestMeeting')
    
    #def test_tablename(self):
        #self.assertEqual(str(MeetingMinutes._meta.db_table), 'meetingminutes')

