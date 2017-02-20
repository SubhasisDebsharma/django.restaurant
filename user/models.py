from django.db import models


class UserDetails(models.Model):
    USER_TYPE_CUSTOMER = "customer"
    USER_TYPE_OFFICE = "kitchen"

    user_type_choice = (
        (USER_TYPE_CUSTOMER, "Customer"),
        (USER_TYPE_OFFICE, "Office")
    )

    userid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=13,null=True)
    address = models.CharField(max_length=200)
    user_type = models.CharField(max_length=100, choices=user_type_choice)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'user_details'

