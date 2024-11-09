from django.db import models
# from django.utils import timezone
import datetime
# from datetime import date

# Create your models here.
class User(models.Model):
    # def save(self, *args, **kwargs):
    #     if not self.id:  # If the instance is being created
    #         self.created_date = timezone.now()
    #     self.modified_date = timezone.now()  # Update modified_date on every save
    #     super(User, self).save(*args, **kwargs)
        
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.BigIntegerField()
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    verified = models.BooleanField(default=False, editable=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    position = models.ForeignKey('Position', on_delete=models.SET_NULL, null=True, blank=True)
    leaves = models.IntegerField(default=10, editable=False)
    annual_salary = models.IntegerField(default=None, null=True, blank=True, editable=False)
    # created_date = models.DateTimeField(default=timezone.now, editable=False)
    # modified_date = models.DateTimeField(default=timezone.now,editable=False)

    def __str__(self):
        return f"{self.first_name}{self.last_name}"
        # return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = 'user'
    
    
class Employer(models.Model):
    # def save(self, *args, **kwargs):
    #     if not self.id:  # If the instance is being created
    #         self.created_date = timezone.now()
    #     self.modified_date = timezone.now()  # Update modified_date on every save
    #     super(User, self).save(*args, **kwargs)
        
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.BigIntegerField()
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'employer'
        

class Position(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self): 
        return self.name

    class Meta: 
        db_table = 'position'
  
class LeaveManage(models.Model): #payroll_app_leavemanage table name
    STATUS_CHOICES = (
    ('pending', 'Pending'), 
    ('approved', 'Approved'),
    ('rejected', 'Rejected'),
    )
    
    user = models.ForeignKey('User', on_delete = models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self): 
        return f"{self.user}"
    
    class Meta: 
        db_table = 'leavemanage'
 
 
def year_choices():
     return [(r,r) for r in range(1984, datetime.date.today().year + 1)]
    
def current_year():
    return datetime.date.today().year


class PayrollManagement(models.Model):
    MONTH_CHOICES = (
        (1, 'January'),
        (2, 'February'),
        (3, 'March'),
        (4, 'April'),
        (5, 'May'),
        (6, 'June'),
        (7, 'July'),
        (8, 'August'),
        (9, 'September'),
        (10, 'October'),
        (11, 'November'),
        (12, 'December')
    )
    user = models.ForeignKey('User', on_delete = models.CASCADE)
    year = models.IntegerField(
        choices=year_choices(),
        default=current_year()
    )
    
    month = models.IntegerField(choices=MONTH_CHOICES)
    gross_salary = models.FloatField(null=True, blank=True)
    provident_fund = models.FloatField(null=True, blank=True)
    professional_tax = models.FloatField(null=True, blank=True)
    loss_of_pay = models.FloatField(default=0.00)
    net_salary = models.FloatField(null=True, blank=True)
    
    def __str__(self): 
        return f"{self.user}"
    
    class Meta:
        db_table = 'payrollmanagement'
    
    


# income_tax = models.IntegerField()
# class UserSignup(models.Model):
#     def save(self, *args, **kwargs):
#         if not self.id:  # If the instance is being created
#             self.created_date = timezone.now()
#         self.modified_date = timezone.now()  # Update modified_date on every save
#         super(User, self).save(*args, **kwargs)
        
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     phone_number = models.IntegerField(default=0000000000)
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=100)
#     verified = models.BooleanField(default=False)
#     created_date = models.DateTimeField(default=timezone.now, editable=False)
#     modified_date = models.DateTimeField(default=timezone.now,editable=False)

#     def __str__(self):
#         return self.email

#     class Meta:
#         db_table = 'usersignup' 
        
        
# user -
# ---------------------------------
# first_name - string field
# last_name - string field
# phone_number - int field
# email - email field, unique
# password  -string field
# verified - boolean field -default False
# created-date- datetime field - default datetime now
# modified-date- datetime field  - default datetime now

# employer -
# ----------------------------
# first_name
# last_name
# phone_number
# email - , unique
# password
# created-date - default datetime now
# modified-date - default datetime now

# def save(self, *args, **kwargs):
#         self.modified_date = timezone.now()
#         super().save(*args, **kwargs)