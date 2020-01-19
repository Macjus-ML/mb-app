from django.db import models

class Post(models.Model):
    text = models.TextField()

    def __str__(self):
        """Строковое отображение модели """
        return self.text[:50]
