from django.db import models

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField(blank=True, null=True)

    is_first = models.BooleanField(default=False)

    # Old code - For connecting option to next question
    # option = models.ForeignKey('Option', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

class Option(models.Model):
    description = models.CharField(max_length=256)
    # How is this option related to it's parent question
    related_question = models.ForeignKey('Question', on_delete=models.CASCADE, related_name='options')

    # The question to go after choosing this option
    next_question = models.ForeignKey('Question', on_delete=models.SET_NULL, null=True, blank=True)

    # Specify language if it is a final option
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.description

class Language(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

