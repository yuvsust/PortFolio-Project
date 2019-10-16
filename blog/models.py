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

    #Show the object name in Admin Page
    def __str__(self):
        return self.title

    # this is for blog home page
    # We dont want to show whole post in tha home. we will show only the summary
    def summary(self):
        return self.body[:80]

    #Formatting the Date
    #Oct 15 2019
    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

