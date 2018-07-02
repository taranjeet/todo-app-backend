from django.db import models


class Todo(models.Model):

    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'todo'

    def __str__(self):
        return '{}'.format(self.title)
