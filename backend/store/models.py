from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=75)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE,
                               related_name='subcategories',
                               null=True, blank=True)

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
    stock = models.IntegerField(default=0)
    in_stock = models.CharField(choices=STOCK_CHOICES)

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

    def save(self, *args, **kwargs):
        self._update_in_stock_status()
        super().save(*args, **kwargs)


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Image for - {self.product}'