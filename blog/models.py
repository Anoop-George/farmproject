from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
from django.db.models import IntegerField, Model
from django.core.validators import MaxValueValidator, MinValueValidator



class Post(models.Model):
    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    GRADUATE = 'GR'
    YEAR_IN_SCHOOL_CHOICES = [
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
        (GRADUATE, 'Graduate'),
    ]

    district=models.CharField(max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES)

    title = models.CharField(max_length=300)
    mobile= models.IntegerField(
        validators=[
            MaxValueValidator(99999999999),
            MinValueValidator(999999)
        ]) #update this to number
    price=models.IntegerField(default=1,
        validators=[
            MaxValueValidator(99999999999),
            MinValueValidator(1)
        ]) #update this to number
    catagory=models.CharField(max_length=100)
    buyorsell=models.CharField(max_length=3)
    content = models.CharField(max_length=3200)
    pincode= models.IntegerField(null=True,blank=True,
        validators=[
            MaxValueValidator(999999),
            MinValueValidator(100000)
        ])
    state=models.CharField(max_length=225,null=True,blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image1 = models.ImageField(default='default.jpg', upload_to='post_pics',null=True,blank=True)
    image2 = models.ImageField(default='default.jpg', upload_to='post_pics',null=True,blank=True)
    image3 = models.ImageField(default='default.jpg', upload_to='post_pics',null=True,blank=True)
    image4 = models.ImageField(default='default.jpg', upload_to='post_pics',null=True,blank=True)

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





