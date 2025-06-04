from django.db import models

# Create your models here.

from students.models import BaseClass

class StatusChoices(models.TextChoices):

    PENDING = 'Pending' , 'Pending'

    SUCCESS = 'Success' , 'Success'

    FAILED = 'Failed' , 'Failed'

class Payment(BaseClass):

    student = models.ForeignKey('students.Students',on_delete=models.CASCADE)

    course = models.ForeignKey('courses.Courses',on_delete=models.CASCADE)

    amount = models.FloatField()

    status = models.CharField(max_length=15,choices=StatusChoices.choices,default=StatusChoices.PENDING)

    paid_at = models.DateTimeField(null=True,blank=True)

    def __str__(self):

        return f'{self.student.name}-{self.course.title}-{self.amount}'
    
    class Meta:

        verbose_name = 'Payments'

        verbose_name_plural = 'Payments'

class Transaction(BaseClass):

    Payment = models.ForeignKey('Payment',on_delete=models.CASCADE)  

    rzp_order_id = models.SlugField(null=True,blank=True)

    status = models.CharField(max_length=15,choices=StatusChoices.choices,default=StatusChoices.PENDING)

    transaction_at = models.DateTimeField(null=True,blank=True)

    rzp_payment_id = models.SlugField(null=True,blank=True)

    rzp_payment_signature = models.TextField(null=True,blank=True)

    def __str__(self):

        return f'{self.Payment.student.name}-{self.course.title}-Transaction'
    
    class meta:

        verbose_name ='Transactions'

        verbose_name_plural ='Transactions'



