from django.db import models

class Page(models.Model):
    filtered_image = models.ImageField(upload_to='%Y/%m/%d/filtered')
    image = models.ImageField(upload_to='%Y/%m/%d/orig')
    content = models.TextField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def delete(self, *args, **kwargs):
        self.image.delete()
        self.filtered_image.delete()
        super(Page, self).delete(*args, **kwargs)
