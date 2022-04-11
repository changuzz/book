from django.db import models
class Books(models.Model):
    book_name=models.CharField(max_length=100,unique=True)
    author=models.CharField(max_length=100)
    amount =models.PositiveIntegerField()
    copies=models.PositiveIntegerField()
    image=models.ImageField(upload_to="images",null=True)
    def __str__(self):
        return self.book_name


#ORM
#ref= ModelName(property=value,property=value,property=value)
#ref.save()

