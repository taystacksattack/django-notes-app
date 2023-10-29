from django.db import models

class Note(models.Model):
    body = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True) #auto_now will update on each save
    created = models.DateTimeField(auto_now_add=True) #auto_now_add is recorded ONLY ONCE (when it's created)

    def __str__(self):
        return self.body[0:50]
