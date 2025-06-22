from rest_framework import viewsets
from webapp.models import (
    LearningPreference, Course, Module, Section, Lesson,
    UserCourseProgress, RecentActivity
)
from webapp.serializers import (
    LearningPreferenceSerializer, CourseSerializer, ModuleSerializer,
    SectionSerializer, LessonSerializer, UserCourseProgressSerializer,
    RecentActivitySerializer
)
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class LearningPreferenceViewSet(viewsets.ModelViewSet):
    queryset = LearningPreference.objects.all()
    serializer_class = LearningPreferenceSerializer

class ModuleViewSet(viewsets.ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer

class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class UserCourseProgressViewSet(viewsets.ModelViewSet):
    queryset = UserCourseProgress.objects.all()
    serializer_class = UserCourseProgressSerializer

class RecentActivityViewSet(viewsets.ModelViewSet):
    queryset = RecentActivity.objects.all()
    serializer_class = RecentActivitySerializer