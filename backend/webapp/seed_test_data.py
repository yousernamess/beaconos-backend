from django.contrib.auth import get_user_model
from webapp.models import (
    LearningPreference,
    Course,
    Module,
    Section,
    Lesson,
    UserCourseProgress,
    RecentActivity
)
from datetime import date

User = get_user_model()

def run():
    # 1. Create test user
    user, _ = User.objects.get_or_create(username='testuser', email='test@example.com')
    user.set_password('testpass')
    user.save()

    # 2. Create learning preference
    preference, _ = LearningPreference.objects.get_or_create(
        user=user,
        topic='Python',
        goal='Become a backend developer',
        experience_level='beginner',
        time_commitment='3_to_6',
        learning_style='reading'
    )

    # 3. Create course
    course, _ = Course.objects.get_or_create(
        user=user,
        learning_preference=preference,
        title='Learn Python Fundamentals',
        description='An introductory course for new Python developers'
    )

    # 4. Create module
    module, _ = Module.objects.get_or_create(
        course=course,
        title='Week 1: Python Basics',
        description='Learn the basics of Python syntax and data types.',
        order=1
    )

    # 5. Create section
    section, _ = Section.objects.get_or_create(
        module=module,
        title='Introduction to Python',
        description='Setup and Hello World',
        order=1
    )

    # 6. Create lesson
    lesson, _ = Lesson.objects.get_or_create(
        section=section,
        title='Hello World in Python',
        content='Use print("Hello, World!") to print.',
        objectives='Understand the basic print function',
        order=1
    )

    # 7. Create user progress
    UserCourseProgress.objects.get_or_create(
        user=user,
        course=course,
        hours_learned=1.5,
        is_completed=False,
        current_streak=2,
        last_active=date.today()
    )

    # 8. Create recent activity
    RecentActivity.objects.get_or_create(
        user=user,
        course=course,
        lesson=lesson
    )

    print("✅ Seed data created successfully.")
