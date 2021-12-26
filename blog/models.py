from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

class Post(models.Model):
    title = models.CharField(max_length=300)
    mobile= models.CharField(max_length=12) #update this to number
    price=models.CharField(max_length=12) #update this to number
    catagory=models.CharField(max_length=22)
    buyorsell=models.CharField(max_length=3)
    content = models.CharField(max_length=2200)
    pincode= models.CharField(max_length=6,blank=True,null=True)#update this to number
    district=models.CharField(max_length=225)
    state=models.CharField(max_length=225)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image1 = models.ImageField(default='default.jpg', upload_to='post_pics')
    image2 = models.ImageField(default='default.jpg', upload_to='post_pics')
    image3 = models.ImageField(default='default.jpg', upload_to='post_pics')
    image4 = models.ImageField(default='default.jpg', upload_to='post_pics')

    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)

        img1 = Image.open(self.image1.path)
        img2 = Image.open(self.image2.path)
        img3 = Image.open(self.image3.path)
        img4 = Image.open(self.image4.path)

        if img1.height > 400 or img1.width > 400:
            output_size = (400,400)
            img1.thumbnail(output_size)
            img1.save(self.image1.path)      

        if img2.height > 400 or img2.width > 400:
            output_size = (400,400)
            img2.thumbnail(output_size)
            img2.save(self.image2.path)      

        if img3.height > 400 or img3.width > 400:
            output_size = (400,400)
            img3.thumbnail(output_size)
            img3.save(self.image3.path)
       
        if img4.height > 400 or img4.width > 400:
            output_size = (400,400)
            img4.thumbnail(output_size)
            img4.save(self.image4.path)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})





