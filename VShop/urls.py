from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('api/Account/', include('base.urls')),
    path('api/Account/', include('seller.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),
    path('api/products/', include('seller.urls')),
    path('api/products/', include('seller_product.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
