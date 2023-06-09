from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('web.ulrs')),
    path('shop/', include('Product.urls')),
    path('account/', include('account.urls')),
    path('cart/', include('cart.urls')),
    path('blog/', include('blog.urls')),
    path('zarinpal/', include('zarinpal.urls')),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
