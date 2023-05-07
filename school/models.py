from django.db import models

# Create your models here.
class user(models.Model):
    first_name = models.CharField(max_length=30,null=False)
    last_name = models.CharField(max_length=30)
    phone = models.IntegerField()
    email = models.EmailField(blank = False)
    date_of_birth = models.DateField()
    mark1 = models.IntegerField(default='5')
    course = models.CharField(max_length=30)
    address=models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    qualification= models.CharField(max_length=30,default='Qualification')
    parent_name = models.CharField(max_length=30,default='name')
    parent_number = models.IntegerField(max_length=30,default='000')
    parent_occupation = models.CharField(max_length=30,default='occupation')
    def __str__(self):
        return self.first_name
                 
class student_details(models.Model):
    start_name = models.CharField(max_length=30)
    start_phone = models.IntegerField()
    start_email = models.EmailField()

    def __str__(self):
        return self.start_name
    

class cards(models.Model):
    image=models.ImageField(blank=False)
    heading=models.CharField(max_length=30,blank=False)
    text=models.TextField(blank=False)
    fees=models.IntegerField(blank=False)
    offerfees=models.IntegerField(blank=True,default='0')
    duration=models.IntegerField(blank=False)
    

    def __str__(self):
        return self.heading


