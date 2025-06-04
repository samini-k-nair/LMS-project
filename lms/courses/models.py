from django.db import models

import uuid


#category_choice =[
   # ('IT & Softwares','IT & Softwares')
   # ('')
#]
class CategoryChoices(models.TextChoices):

   # variable='value','representation'

   IT_SOFTWARES = 'IT & Softwares','IT & Softwares'

   FINANCE = 'Finance','Finance'

   MARKETING = 'Marketing','Marketing'

class BaseClass(models.Model):

   uuid = models.SlugField(unique=True,default=uuid.uuid4)

   active_status = models.BooleanField(default=True)

   created_at = models.DateTimeField(auto_now_add=True)

   updated_at = models.DateTimeField(auto_now=True)

   class Meta:

     abstract=True

class LevelChoices(models.TextChoices):

   BEGINNER = 'Beginner','Beginner' 

   INTERMEDIATE ='intermediate','intermediate'    

   ADVANCED ='advanced','advanced'

class TypeChoices(models.TextChoices):

   FREE = 'Free','Free' 

   PREMIUM ='Premium','Premium'    


class Courses(BaseClass):# table name

    title = models.CharField(max_length=50)# field,data type,constraints

    description = models.TextField()

    image = models.ImageField(upload_to='course-images/')#

    instructor = models.ForeignKey('instructors.Instructors',on_delete=models.CASCADE)
                                   # app name.model name
                                   
   # category = models.CharField(max_length=25,choice=category_choice) defining choices as list of tuple method

    category = models.CharField(max_length=25,choices=CategoryChoices.choices)# defining choices as class by inherit textchoices class

    level = models.CharField(max_length=25,choices=LevelChoices.choices)

    type = models.CharField(max_length=15,choices=TypeChoices.choices)

    tags = models.TextField()

    fee = models.DecimalField(max_digits=8,decimal_places=2)

    offer_fee = models.DecimalField(max_digits=8,decimal_places=2,null=True,blank=True)

    def __str__(self):
       
      return f'{self.title}-{self.instructor}'
    
    class Meta:

      verbose_name = 'Courses'

      verbose_name_plural = 'Courses'    

      ordering =['id']