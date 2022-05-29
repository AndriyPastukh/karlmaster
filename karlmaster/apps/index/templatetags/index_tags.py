from django import template
from index.models import *



register = template.Library()


@register.inclusion_tag('index/slider_tag.html')
def slider():
    imgs = Slider.objects.all()
    
    return {"imgs":imgs}


@register.inclusion_tag('index/testimonials.html')
def testimonials():
    testimonials = Testimonials.objects.all()
    
    return {"testimonials":testimonials}


