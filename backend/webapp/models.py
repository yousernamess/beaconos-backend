from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class LearningPreference(models.Model):
    EXPERIENCE_LEVEL_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]

    TIME_COMMITMENT_CHOICES = [
        ('less_than_3', 'Less than 3 hours/week'),
        ('3_to_6', '3–6 hours/week'),
        ('more_than_6', 'More than 6 hours/week'),
    ]

    LEARNING_STYLE_CHOICES = [
        ('visual', 'Visual'),
        ('reading', 'Reading/Writing'),
        ('audio', 'Audio'),
        ('interactive', 'Interactive'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.CharField(max_length=255)
    goal = models.TextField(blank=True, null=True)
    experience_level = models.CharField(max_length=20, choices=EXPERIENCE_LEVEL_CHOICES)
    time_commitment = models.CharField(max_length=20, choices=TIME_COMMITMENT_CHOICES)
    learning_style = models.CharField(max_length=20, choices=LEARNING_STYLE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s preference for {self.topic}"
    

class Course(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    learning_preference = models.ForeignKey('LearningPreference', on_delete=models.PROTECT)

    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)  # Rahul edited this line by himself
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} (for {self.user.username})"


class Module(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='modules')
    title = models.CharField(max_length=255)
    description = models.TextField()
    order = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order']
        unique_together = ('course', 'order')

    def __str__(self):
        return f"{self.title} (Module {self.order})"
    

class Section(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='sections')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    order = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order']
        unique_together = ('module', 'order')

    def __str__(self):
        return f"{self.title} (Section {self.order})"


class Lesson(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=255)
    content = models.TextField()
    objectives = models.TextField(blank=True, null=True)
    order = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order']
        unique_together = ('section', 'order')

    def __str__(self):
        return f"{self.title} (Lesson {self.order})"
    
    
class UserCourseProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='progress')
    hours_learned = models.FloatField(default=0.0)
    is_completed = models.BooleanField(default=False)
    current_streak = models.PositiveIntegerField(default=0)
    last_active = models.DateField(auto_now=True)

    class Meta:
        unique_together = ('user', 'course')

    def __str__(self):
        return f"{self.user.username}'s progress on {self.course.title}"


class RecentActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    viewed_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-viewed_at']
        unique_together = ('user', 'lesson')

    def __str__(self):
        return f"{self.user.username} viewed {self.lesson.title} on {self.viewed_at}"



