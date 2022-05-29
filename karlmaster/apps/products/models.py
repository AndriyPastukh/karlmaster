from distutils.command.upload import upload
from email.policy import default
from django.db import models



# class NewArrivals(models.Model):
#     pass


class Size(models.Model):
    clothes_size = models.IntegerField('size')
    def __str__(self):
        return "Size: " + str(self.clothes_size)   




class ProductImages(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to = 'imagesProduct/')
    default = models.BooleanField(default=False)


    def __str__(self):
        return str(self.name)   


class Product(models.Model):
    name = models.CharField('name', max_length=100)
    price = models.IntegerField('price', )
    info = models.TextField('information ', max_length=700)
    cart_detail = models.TextField('cart details', max_length=700)
    feedback_choices = (
        (1, 'bad'),
        (2, 'below average'),
        (3, 'middle'),
        (4, 'good'),
        (5, 'best'),
    )
    feedback = models.IntegerField(choices=feedback_choices ,verbose_name='FeedBack')
    shiping_returns = models.TextField('shiping and returns', max_length=1000)

    is_available = models.BooleanField('available', default=True)

    size = models.ManyToManyField(Size, related_name='size', null=True)
    images = models.ManyToManyField(ProductImages, blank=True)

    slug= models.SlugField('slug', )
    
    def __str__(self):
        return  self.name  

    




class Category(models.Model):
    # product = models.ForeignKey('product', on_delete=models.CASCADE)
    name = models.CharField('category name',max_length=20)



