from django.db import models

class pharjinny_registration(models.Model):
     email_id=models.EmailField(max_length=255)
     password = models.CharField(max_length=20)
     confirm_password=models.CharField(max_length=20)
     first_name = models.CharField(max_length=30)
     last_name = models.CharField(max_length=30)
     DOB = models.DateField(blank=True, null=True)
     gender = (("M", "Male"), ("F", "Female"))
     gender = models.CharField(max_length=1, choices=gender, default="M", null=False)
     contact_no=models.CharField(max_length=13)
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)

     def __unicode__(self):
          return self.email_id, self.password,self.confirm_password,self.first_name,self.last_name,self.DOB,self.gender,self.contact_no


class likes(models.Model):
     pharjinny_registration_id=models.CharField(max_length=10)
     #status=models.CharField(max_length=12)
     #comments=models.CharField(max_length=255)
     content=models.CharField(max_length=255)
     photo=models.FileField(upload_to='upload')
     video=models.FileField(upload_to='upload')
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)

class mass_post(models.Model):
     content_id=models.CharField(max_length=10)
     user_id=models.CharField(max_length=10)
     status=models.CharField(max_length=255)
     comment=models.CharField(max_length=255)
     photo=models.ImageField(upload_to='upload')
     video = models.FileField(upload_to='upload')
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)
