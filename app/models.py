from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Seller(BaseModel):
    full_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="media/Seller_image",null=True,blank=True)
    backgroud_image = models.ImageField(upload_to="media/Seller_backgroud_image",null=True,blank=True)
    sold =  models.IntegerField(null=True,blank=True)
    income = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return self.full_name

class Category(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    icon = models.ImageField(upload_to='media/category_icons/')

    def __str__(self):
        return self.name

class Product(BaseModel):
    file_type = [
        ('pptx', 'Pptx'),
        ('pdf', 'Pdf'),
        ('docx', 'Docx'),
    ]

    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name="products")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="products")
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    pages = models.IntegerField()
    file_size = models.FloatField(help_text="File size in MB")
    file_type = models.CharField(max_length=10,choices=file_type)  # pptx, pdf, docx, etc.
    file = models.FileField(upload_to="media/products/")
    

    def __str__(self):
        return self.title

