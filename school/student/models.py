from django.db import models
from email.mime import image

# Create your models here.



BIrthCountry= (
    ('Egypt','Egypt'),
    ('Japan','Japan'),
    ('Brazil','Brazil'),
)


Gander= (
    ('male','male'),
    ('female','female'),
)


REigon= (
    ('Reigon x','Reigon x'),
    ('Reigon z','Reigon z'),
    ('Reigon y','Reigon y'),
)


REigonSector= (
    ('Region Sector x','Region Sector x'),
    ('Region Sector z','Region Sector z'),
    ('Region Sector y','Region Sector y'),
)

NAtionalty= (
    ('United Kingdom','United Kingdom'),
    ('Uruguay','Uruguay'),
    ('United States','United States'),
)

NAtionaltyCategory= (
    ('United Kingdom','United Kingdom'),
    ('Uruguay','Uruguay'),
    ('United States','United States'),
)

MaritalStatus= (
    ('single','single'),
    ('married','married'),
)

class Student(models.Model):
    NationaliD= models.TextField(max_length=50 ,blank=True,null=True)
    InformationSource= models.TextField(max_length=100 ,blank=True,null=True)
    FullName= models.TextField(max_length=50 ,blank=True,null=True)
    FirstName = models.TextField(max_length=50)
    SecondName=models.TextField(max_length=50 ,blank=True,null=True)
    ThirdName=models.TextField(max_length=50 ,blank=True,null=True)
    FourthName=models.TextField(max_length=50 ,blank=True,null=True)
    FamilyName=models.TextField(max_length=50)
    EnglishName=models.TextField(max_length=50 ,blank=True,null=True)
    EnglishFirstName =models.TextField(max_length=50)
    EnglishSecondName=models.TextField(max_length=50 ,blank=True,null=True)
    EnglishThirdName=models.TextField(max_length=50 ,blank=True,null=True)
    EnglishFourthName=models.TextField(max_length=50 ,blank=True,null=True)
    EnglishFamilyName =models.TextField(max_length=50)
    BirthName=models.TextField(max_length=50 ,blank=True,null=True)
    BirthData =models.DateField()
    age=models.IntegerField() 
    BirthCity= models.TextField(max_length=50 ,blank=True,null=True)
    EnglishBirthCity= models.TextField(max_length=50 ,blank=True,null=True)
    BirthCountry = models.CharField(max_length=50,choices=BIrthCountry)
    gander= models.CharField(max_length=50,choices=Gander)
    maritalStatus= models.CharField(max_length=50,choices=MaritalStatus,blank=True,null=True)
    Reigon = models.CharField(max_length=50,choices=REigon)
    ReigonSector= models.CharField(max_length=50,choices=REigonSector,blank=True,null=True)
    Nationalty= models.CharField(max_length=50,choices=NAtionalty)
    NationaltyCategory= models.CharField(max_length=50,choices=NAtionaltyCategory)
    image = models.ImageField(upload_to='profile/', height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return self.FirstName