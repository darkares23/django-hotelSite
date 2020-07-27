from django.db import models

# Create your models here.
property_types = (('Sale', 'Sale'), ('Rent', 'Rent'))
objects = models.Manager()


class Property(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50, null=True)
    type = models.CharField(choices=property_types, max_length=20)
    price = models.IntegerField()
    category = models.ForeignKey(
        'Category', null=True, on_delete=models.SET_NULL)
    area = models.DecimalField(decimal_places=2, max_digits=8)
    beds_number = models.PositiveIntegerField()
    baths_number = models.PositiveIntegerField()
    garages_number = models.PositiveIntegerField()
    image = models.ImageField(upload_to='property/', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Property'
        verbose_name_plural = 'Properties'


class Category(models.Model):
    category_name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='category/', null=True)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Reserve(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    notes = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Reserve'
        verbose_name_plural = 'Reserves'
