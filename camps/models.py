from django.db import models

# Create your models here.


class Category(models.Model):
    """ This is the camp categories. For example, EU or UK Camp """

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Camp(models.Model):
    """ This is the camp details model. """
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    finish_date = models.DateField()
    location = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    coaches = models.CharField(max_length=100)
    staff = models.CharField(max_length=100)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
