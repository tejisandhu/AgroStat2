from django.db import models


# Create your models here.
class person(models.Model):
     F_name=models.CharField(max_length=35)
     L_name=models.CharField(max_length=35)
     

class FAQ(models.Model):
     ques=models.TextField()
     ans=models.TextField()
     def __str__(self):
          return self.ques


class Agriculture_Universities(models.Model):
     name=models.CharField(max_length=50)
     established=models.CharField(max_length=5)
     director=models.CharField(max_length=30)
     image=models.ImageField(upload_to="University",blank=True) 
     address=models.CharField(max_length=100,null=True)
     website=models.URLField()    
     def __str__(self):
          return self.name

class Agriculture_News(models.Model):
     title=models.CharField(max_length=200)
     sub_title=models.CharField(max_length=200,blank=True)
     date=models.CharField(max_length=100,blank=True)
     reporter=models.CharField(max_length=50,blank=True)
     description=models.TextField()
     image=models.ImageField(upload_to="News",blank=True) 
     photographer=models.CharField(max_length=100,blank=True)
     
     

class Agriculture_Videos(models.Model):
     title=models.CharField(max_length=50)
     description=models.TextField()
     video=models.FileField()
     
class Agriculture_Crop(models.Model):
     crop_identity=models.CharField(max_length=50,blank=True)
     crop_type=models.CharField(max_length=50)
     image=models.ImageField(upload_to="Crop",blank=True) 
     description=models.TextField()
     video=models.FileField()
     def __str__(self):
          return self.crop_identity
     

class agri_crops_details(models.Model):
     crop_identity=models.CharField(max_length=50,blank=True)
     crop_head=models.CharField(max_length=100)
     image1=models.ImageField(upload_to="Crop",blank=True) 
     image2=models.ImageField(upload_to="Crop",blank=True) 
     para1=models.TextField()
     para2=models.TextField()
     para3=models.TextField()
     pdf=models.FileField(upload_to="crop_pdf",blank=True)
     def __str__(self):
          return self.crop_head
     

class disease_solution(models.Model):
     description=models.CharField(max_length=200,blank=True)
     disease=models.CharField(max_length=50,blank=True)
     title=models.CharField(max_length=200,blank=True)
     detail=models.TextField()
     def __str__(self):
          return self.disease
     
     
     
class Agriculture_Call_centre(models.Model):
     title=models.CharField(max_length=50)
     detail=models.TextField()
     image=models.ImageField(upload_to="Call Centre",blank=True) 
     def __str__(self):
          return self.title

class Agriculture_Farmer_Scheme(models.Model):
     title=models.CharField(max_length=50)
     description=models.TextField()
     pdf=models.FileField()
     def __str__(self):
          return self.title

class Latest_Technology(models.Model):
     name=models.CharField(max_length=50) 
     description=models.TextField()
     photo=models.ImageField(upload_to="Technology",blank=True) 
     pdf=models.FileField(upload_to="Technology",blank=True)
     def __str__(self):
          return self.name
     



class Indian_Agriculture_University(models.Model):
     name=models.CharField(max_length=50)
     established_in=models.CharField(max_length=5,null=True)
     director_is=models.CharField(max_length=30,null=True)
     #image=models.ImageField(upload_to="University",blank=True)   
     photo=models.ImageField(upload_to="Indian University",blank=True)

     address_is=models.CharField(max_length=100,null=True)
     website_is=models.URLField(null=True)
     def __str__(self):
          return self.name
     
class myreview(models.Model):
     title=models.CharField(max_length=50)
     message=models.TextField()
     def __str__(self):
          return self.title
     
class support(models.Model):
     title=models.CharField(max_length=50)
     content=models.TextField()
     def __str__(self):
          return self.title
     
class contact(models.Model):
     name=models.CharField(max_length=50)
     email=models.EmailField()
     message=models.TextField()
     def __str__(self):
          return self.name

class register(models.Model):
     name=models.CharField(max_length=50)
     email=models.EmailField()
     password=models.CharField(max_length=50)
     contact=models.CharField(max_length=15,blank=True, null=True)
     address=models.TextField(blank=True, null=True)
     gender=models.CharField(max_length=1,blank=True, null=True)
     age=models.CharField(max_length=15,blank=True, null=True)
     profile_picture=models.ImageField(upload_to="ProfilePictures",default="DP_2.jpg",blank=True)
     def __str__(self):
          return self.email
     
class ChatMessage(models.Model):
     user = models.CharField(max_length=100)
     message = models.TextField()
     created_at = models.DateTimeField(auto_now_add=True)
     
     
class newsletter(models.Model):
     email=models.EmailField()
     def __str__(self):
          return self.email
     
class dealers(models.Model):
     name=models.CharField(max_length=100)
     address=models.TextField(blank=True, null=True)
     phone=models.CharField(max_length=100)
     website=models.URLField(null=True)   
     image=models.ImageField(upload_to="Dealers",blank=True)
     def __str__(self):
          return self.name
      
     
     
     
          


#model name and view page name should not be same
# whenever make a change in the models always need to run
#also register the model to the admin.py
# python  manage.py migrate 
# python  manage.py makemigrations myapp 
# python  manage.py migrate         


#python manage.py startapp myapp         to make a folder
