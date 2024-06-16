from django.db import models



# Create your models here.


class Category(models.Model):
    tile1=models.CharField(max_length=200)
    limit =models.IntegerField()
    slug=models.CharField(max_length=200)
    def __str__(self):
        return self.tile1


class Post(models.Model):
    CONTENT_TYPES = (
        ('slider', 'Slider'),
        ('card', 'Card'),
        ('testimonial', 'Testimonial'),
        ('gallery','Gallery'),
        ('galleryimages','Galleryimages'),
        ('aboutus','Aboutus'),
        ('aboutimages','Aboutimages'),
        ('contact','Contact')
    )
    title=models.CharField(max_length=200)
    category= models.ForeignKey(Category, on_delete=models.CASCADE)
    job_title= models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    image=models.ImageField(upload_to="image",null=True,blank=True)
    content_type = models.CharField(max_length=20, choices=CONTENT_TYPES)
    def __str__(self):
        return self.title
    


