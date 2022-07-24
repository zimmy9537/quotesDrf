from django.db import models

class Quotelist(models.Model):
    quoteContent=models.CharField(max_length=500)
    quoteAuthor=models.CharField(max_length=100)
    
    def __str__(self):
        return self.quoteContent
    