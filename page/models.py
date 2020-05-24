from django.db import models
from django.urls import reverse_lazy

from django.contrib.auth import get_user_model

from django.conf import settings


class Page(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    filtered_image = models.ImageField(upload_to='%Y/%m/%d/filtered')
    image = models.ImageField(upload_to='%Y/%m/%d/orig')
    content = models.TextField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at', '-pk', )    
    
    def delete(self, *args, **kwargs):
        self.image.delete()
        self.filtered_image.delete()
        super(Page, self).delete(*args, **kwargs)

    def get_absolute_url(self):
        url = reverse_lazy('detail', kwargs={'pk': self.pk})
        
        return url