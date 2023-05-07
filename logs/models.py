from django.db import models

class Topic(models.Model):
    topic=models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.topic


class Entry(models.Model):
    entry=models.ForeignKey(Topic,on_delete=models.CASCADE)
    body=models.TextField()
    date_updated=models.DateTimeField(auto_now=True)
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return self.entry
    

