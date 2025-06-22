from rest_framework import serializers
from .models import Course, LearningPreference, Module, Section, Lesson, UserCourseProgress, RecentActivity

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'user', 'learning_preference', 'title', 'description', 'created_at']

class LearningPreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = LearningPreference
        fields = ['id', 'user', 'topic', 'goal', 'experience_level', 'time_commitment', 'learning_style', 'created_at']



class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ['id', 'course', 'title', 'description', 'order', 'created_at']


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ['id', 'module', 'title', 'description', 'order', 'created_at']


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'section', 'title', 'content', 'objectives', 'order', 'created_at']

class UserCourseProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCourseProgress
        fields = [
            'id',
            'user',
            'course',
            'hours_learned',
            'is_completed',
            'current_streak',
            'last_active'
        ]

class RecentActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = RecentActivity
        fields = ['id', 'user', 'course', 'lesson', 'viewed_at']
