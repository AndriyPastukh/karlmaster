from django.db import models




class Slider(models.Model):
    """here is model of slider on the main page"""
    img = models.ImageField(upload_to="index/slider")
    is_available = models.BooleanField(verbose_name='Published', default=True, null=False, editable=True)
    
class Testimonials(models.Model):
    """here is model of footer comments on the main page"""
    text = models.TextField(max_length=500)
    img = models.ImageField(upload_to="index/Testimonials")
    author = models.CharField(max_length=30)
    livein = models.CharField(max_length=30)
