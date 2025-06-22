def run():
    from webapp.models import (
        LearningPreference, Course, Module, Section, Lesson,
        UserCourseProgress, RecentActivity
    )

    from webapp.serializers import (
        LearningPreferenceSerializer, CourseSerializer, ModuleSerializer,
        SectionSerializer, LessonSerializer, UserCourseProgressSerializer,
        RecentActivitySerializer
    )

    models_and_serializers = [
        (LearningPreference, LearningPreferenceSerializer),
        (Course, CourseSerializer),
        (Module, ModuleSerializer),
        (Section, SectionSerializer),
        (Lesson, LessonSerializer),
        (UserCourseProgress, UserCourseProgressSerializer),
        (RecentActivity, RecentActivitySerializer)
    ]

    for model, serializer_cls in models_and_serializers:
        obj = model.objects.first()
        if obj:
            serializer = serializer_cls(obj)
            print(f"\n✅ {model.__name__} works:")
            print(serializer.data)
        else:
            print(f"\n⚠️ No data found for {model.__name__}")
