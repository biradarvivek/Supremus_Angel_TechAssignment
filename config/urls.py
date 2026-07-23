"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Mini E-Commerce API",
        default_version="v1",
        description="REST API documentation for the Mini E-Commerce Platform",
        contact=openapi.Contact(
            email="vivek@example.com",
        ),
        license=openapi.License(
            name="MIT License",
        ),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Home
    path("", include("core.urls")),

    # Admin
    path("admin/", admin.site.urls),

    # HTML Routes
    path("products/", include("products.urls")),
    path("categories/", include("categories.urls")),
    path("accounts/", include("accounts.urls")),
    path("cart/", include("cart.urls")),
    path("orders/", include("orders.urls")),

    # REST API
    path("api/auth/", include("accounts.api_urls")),
    path("api/categories/", include("categories.api_urls")),
    path("api/products/", include("products.api_urls")),
    path("api/cart/", include("cart.api_urls")),
    path("api/orders/", include("orders.api_urls")),

    # Swagger
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(
        "redoc/",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
