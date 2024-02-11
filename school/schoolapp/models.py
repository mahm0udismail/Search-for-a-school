from django.db import models

# Create your models here.

SchoolType = (
    ('National','National'),
    ('International','International'),
    ('public','public'),
)
SchoolGrade = (
    ('KG1','KG1'),
    ('KG2','KG2'),
    ('1primary','1primary'),
    ('2primary','2primary'),
    ('3primary','3primary'),
    ('4primary','4primary'),
    ('5primary','5primary'),
    ('6primary','6primary'),
    ('1secondary','1secondary'),
    ('2secondary','2secondary'),
    ('3secondary','3secondary'),
)
class School(models.Model):
    school_name = models.TextField() 
    school_code = models.TextField() 
    school_type = models.CharField(max_length=50,choices=SchoolType)
    school_grade = models.CharField(max_length=50,choices=SchoolGrade)

    def __str__(self):
        return self.school_name