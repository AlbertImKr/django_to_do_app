from django.db import models


class List(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name + ' | ' + str(self.description)


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    list = models.ForeignKey(
        List,
        on_delete=models.CASCADE,
        related_name='tasks',
        blank=True,
        null=True,
    )
    PRIORITY_CHOICES = [
        (1, '낮음'),
        (2, '중간'),
        (3, '높음'),
    ]
    priority = models.IntegerField(
        choices=PRIORITY_CHOICES,
        default=2,
    )

    def __str__(self):
        return f"{self.title} (우선순위: {self.get_priority_display()})"
