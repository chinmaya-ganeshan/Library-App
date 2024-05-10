#from django.db import models

# Create your models here.
from django.db import models
# Models
class app(models.Model):
    name = models.CharField(max_length = 50)
    picture = models.ImageField()
    author = models.CharField(max_length = 30, default = 'annonymous')
    email = models.EmailField(blank = True)
    describe = models.TextField(default = 'Easy to Learn')
    def __str__(self):
        return self.name
        
