from django.db import models

# Create your models here.

# Kliento modelis
class Customer(models.Model):
    f_name = models.CharField('First name', max_length=255, null=False, help_text="Enter first name")
    l_name = models.CharField('Last name', max_length=255, null=False, help_text="Enter last name")
    email = models.EmailField('Email', max_length=255, null=False, help_text="Enter email address")

    def __str__(self):
        return f'{self.f_name} {self.l_name}'

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'


# Bendro užsakymo modelis
class Order(models.Model):
    customer_id = models.ForeignKey('Customer', related_name='orders', on_delete=models.CASCADE, null=True)
    date = models.DateField(auto_now_add=True)

    STATUS = (
        ('n', 'New'),
        ('a', 'Accepted'),
        ('r', 'Ready'),
        ('s', 'Shipped'),
        ('e', 'Aborted'),
    )

    status = models.CharField(
        max_length=1,
        choices=STATUS,
        blank=True,
        default='n',
        help_text='Status',
    )

    @property
    def quantity_price(self):
        products = self.productorder.filter(order_id=self.id)
        suma = 0
        for product in products:
            suma += product.product_id.price * product.quantity
        return suma

    def __str__(self):
        return f'{self.customer_id}'

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'


# Produktų kiekio modelis
class ProductOrder(models.Model):
    order_id = models.ForeignKey('Order', related_name='productorder',on_delete=models.CASCADE, null=True)
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField('Quantity', null=False, default=0)

    def __str__(self):
        return f'{self.order_id} {self.product_id} {self.quantity}'




# Produkto modelis
class Product(models.Model):
    name = models.CharField('Product name', max_length=500, null=False, help_text="Enter product name")
    price = models.FloatField('Price', null=True)

    def __str__(self):
        return f'{self.name}'