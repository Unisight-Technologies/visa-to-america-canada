from django.db import models

# Create your models here.


class News(models.Model):

    CHOICES = [
        ('CIC News', 'CIC News'),
        ('Canada.ca', 'Canada.ca')
    ]

    title = models.CharField(max_length=300)
    author = models.CharField(max_length=150, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    description = models.CharField(max_length=600)
    source = models.CharField(max_length=50, choices=CHOICES, default="CIC News")
    url = models.URLField(max_length=300, help_text="Paste the URL of the article that you are creating.")
    image = models.ImageField(upload_to='', default='default.png')

    class Meta:
        verbose_name_plural = "News"

    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url



class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.BigIntegerField()
    subject = models.CharField(max_length=200)
    message = models.CharField(max_length=800)
