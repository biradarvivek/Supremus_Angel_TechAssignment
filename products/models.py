from django.db import models
from django.utils.text import slugify
from django.core.exceptions import ValidationError

from categories.models import Category


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products"
    )

    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)

    description = models.TextField()

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    stock = models.PositiveIntegerField(default=0)

    image = models.ImageField(
        upload_to="products/",
        blank=True,
        null=True
    )

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["name"]),
            models.Index(fields=["price"]),
        ]

    def clean(self):
        if self.price <= 0:
            raise ValidationError("Price must be greater than 0.")

        if self.stock < 0:
            raise ValidationError("Stock cannot be negative.")

    def save(self, *args, **kwargs):
        # Run all model validations
        self.full_clean()

        # Generate slug automatically
        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name