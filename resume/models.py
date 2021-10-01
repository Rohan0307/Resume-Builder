from django.db import models

# Create your models here.

class Resume(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100,default="Rohan")
    contact = models.IntegerField(default="9561384299")
    email = models.EmailField(max_length=30,default="gmail.com")
    address = models.CharField(max_length=100,default="address")
    image = models.ImageField(upload_to='images/',default="https://p.kindpng.com/picc/s/153-1530388_mario-head-png-png-download-people-profile-pic.png")
    linkedln = models.URLField(max_length=30,default="linkedin.com")
    github = models.URLField(max_length=30,default="github.com")
    insta = models.URLField(max_length=30,default="instagram.com")
    skill1 = models.CharField(max_length=30,default=None)
    skill2 = models.CharField(max_length=30,default=None)
    skill3 = models.CharField(max_length=30,default=None)
    skill4 = models.CharField(max_length=30,default=None)
    objective = models.TextField(max_length=200,default=None)
    work1 = models.TextField(max_length=50,default=None)
    work2 = models.TextField(max_length=50,default=None)
    edu1 = models.TextField(max_length=50,default=None)
    edu2 = models.TextField(max_length=50,default=None)
    ih1 = models.TextField(max_length=50,default=None)
    ih2 = models.TextField(max_length=50,default=None)
    ref = models.TextField(max_length=50,default=None)
    created_on = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.name

    class Meta:
        db_table = "myapp_image"

    


