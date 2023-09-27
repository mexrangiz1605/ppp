from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.


class Register(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=500)

    def register(self):
        self.save()

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Register.objects.get(email=email)
        except:
            return False


    def isExists(self):
        if Register.objects.filter(email = self.email):
            return True

        return  False
    
class Login(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.TextField()
    pictures = models.ImageField(upload_to='category')

    def __str__(self):
        return self.name
    
class Food(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='food')
    about = RichTextField()
    ingredient = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.title
    

    def snippet(self):
        return self.about[:20] + '...read mode'
    

class Secondfood(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='food')
    about = RichTextField()
    ingredient = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.title
    

class Fastfood(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='food')
    about = RichTextField()
    ingredient = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.title
    

class Desert(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='food')
    about = RichTextField()
    ingredient = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.title
    
    
class About(models.Model):
    description = RichTextField()


class Contact(models.Model):
    fullname = models.CharField(max_length=200)
    email = models.EmailField()
    phonenumber = models.IntegerField()
    message = models.TextField()

    def __str__(self):
        return self.fullname
    
class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery')
    
class News(models.Model):
    title = models.CharField(max_length=200)
    about = RichTextField()
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title
    
class Order(models.Model):
    product = models.ForeignKey(Food,on_delete=models.CASCADE)
    customer = models.ForeignKey(Register,on_delete=models.CASCADE)
    quentity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):   
            return Order.objects.filter(customer=customer_id).order_by('-date')
    
class Cart(models.Model):
    name = models.ForeignKey(Food,on_delete=models.CASCADE,related_name='cartname')
    quentity = models.IntegerField(default=1)
    price = models.ForeignKey(Food,on_delete=models.CASCADE,related_name='cartprice')
    total = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name


