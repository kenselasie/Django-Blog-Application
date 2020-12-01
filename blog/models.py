from django.db import models
from users.models import Users

def get_default_profile_image():
    return 'my-images/defaultpic.png/'

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=60)
    subtitle = models.CharField(max_length=60, default=None)
    author = models.ForeignKey(Users, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to="images/userlogo/", null=True, blank=True, default=None)
    text = models.TextField(max_length=3000, default=None, null=True)
    created_at = models.DateTimeField(auto_now_add = True)