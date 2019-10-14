from django.db import models

# Create a Blog Models  (Create a class actually)
# Blog models should have:
    # title
    # publication_date
    # body  ( Text )
    # images

class Blog (models.Model):
    title = models.CharField('Title', max_length = 40)
    pub_date = models.DateTimeField('Post Date')
    body = models.TextField(blank = True)
    image = models.ImageField(upload_to = 'images/')
