from django.db import models

# Create your models here.

class Employee( models.Model ):
    firstName   = models.CharField( max_length = 45 )
    lastName    = models.CharField( max_length = 45 )
    salary      = models.FloatField()
    email       = models.CharField( max_length = 45 )
    pic         = models.CharField( max_length = 50 )


# ----------------------------------------------------------------------------------------------
# relationship Many to Many.
# 1 programmer can be assigned to many projects
# 1 project can have many programmers
# ----------------------------------------------------------------------------------------------


class Programmer( models.Model):
    name = models.CharField( max_length = 20 )
    sal  = models.IntegerField()

class Project(  models.Model ):
    name        = models.CharField( max_length = 30 )
    programmers = models.ManyToManyField( Programmer )


# ----------------------------------------------------------------------------------------------
# relationship 1 to Many. 1 customer has many telephones
# ----------------------------------------------------------------------------------------------

class Customer( models.Model ):
    name = models.CharField( max_length = 30 )

class PhoneNumber( models.Model ):
    type     = models.CharField ( max_length = 10 )
    number   = models.CharField ( max_length = 10 )
    customer = models.ForeignKey( Customer, on_delete = models.CASCADE  )

# ----------------------------------------------------------------------------------------------
# relationship 1 to 1.
# ----------------------------------------------------------------------------------------------
class Person( models.Model ):
    firstName = models.CharField( max_length = 20 )
    lastName  = models.CharField( max_length = 20 )
    age       = models.IntegerField()

class License( models.Model ):
    type      = models.CharField( max_length = 10 )
    validFrom = models.DateField()
    validTo   = models.DateField()
    person    = models.OneToOneField( Person, on_delete = models.CASCADE )



