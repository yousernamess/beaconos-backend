from django.urls import path, include
from rest_framework.routers import DefaultRouter
from webapp.views import (
    CourseViewSet, LearningPreferenceViewSet, ModuleViewSet,
    SectionViewSet, LessonViewSet, UserCourseProgressViewSet,
    RecentActivityViewSet
)

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='course')
router.register(r'learning-preferences', LearningPreferenceViewSet, basename='learningpreference')
router.register(r'modules', ModuleViewSet, basename='module')  # ← this must be here!
router.register(r'sections', SectionViewSet, basename='section')
router.register(r'lessons', LessonViewSet, basename='lesson')
router.register(r'progress', UserCourseProgressViewSet, basename='usercourseprogress')
router.register(r'recent-activity', RecentActivityViewSet, basename='recentactivity')

urlpatterns = [
    path('', include(router.urls)),
]
