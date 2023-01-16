from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from parler.models import TranslatableModel, TranslatedFields

class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Category(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=200),
        slug = models.SlugField(max_length=200,
                                unique=True)
    )

    class Meta:
        # ordering = ['name']
        # indexes = [
        #     models.Index(fields=['name']),
        # ]
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_list_by_category',
                       args=[self.slug])


class Product(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=200),
        slug = models.SlugField(max_length=200),
        description = RichTextField(blank=True, null=True)
    )
    category = models.ForeignKey(Category,
                                 related_name='products',
                                 on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/%Y/%m/%d',
                              blank=True)
    related_images = models.FileField(default="none.jpg", upload_to="related_images")
    
    specifications = RichTextField(blank=True, null=True)
    # description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10,
                                decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    latest = models.BooleanField(default=False, blank=True, null=True)
    top_rated = models.BooleanField(default=False, blank=True, null=True)
    limited_stock = models.BooleanField(default=False, blank=True, null=True)


    class Meta:
        # ordering = ['name']
        indexes = [
            # models.Index(fields=['id', 'slug']),
            # models.Index(fields=['name']),
            models.Index(fields=['-created']),
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail',
                       args=[self.id, self.slug])