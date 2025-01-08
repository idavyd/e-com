from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    pass


class Category(models.Model):
    name = models.CharField(max_length=75)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    icon = models.ImageField(upload_to='category_image/', blank=True, null=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE,
                               related_name='subcategories',
                               null=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f'{self.name}'

    def is_root_category(self):
        return self.parent is None


class Product(models.Model):
    STOCK_CHOICES = (
        ('I', 'IN_STOCK'),
        ('R', 'RUNNING_OUT_OF_STOCK'),
        ('P', 'PREORDER'))
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    short_description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    is_on_sale = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    images = models.ImageField(upload_to='product_images')
    stock = models.IntegerField( default=0)
    in_stock = models.CharField(choices=models.Choices(STOCK_CHOICES))

    def __str__(self):
        return f'{self.name}'

    def update_stock(self, quantity):
        if self.stock + quantity < 0:
            raise ValueError('Not enough stock available')
        else:
            self.stock += quantity
            self.save()

    def _update_in_stock_status(self):
        if self.stock > 15:
            self.in_stock = 'I'
        elif 0 < self.stock <= 15:
            self.in_stock = 'R'
        else:
            self.in_stock = 'P'
        self.save()

    def save(self, *args, **kwargs):
        self._update_in_stock_status()
        super().save(*args, **kwargs)
