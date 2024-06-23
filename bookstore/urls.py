import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from bookstore import views

urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),
    path('admin/', admin.site.urls),
    path('bookstore/v1/', include('order.urls')),
    path('bookstore/v2/', include('order.urls')),
    path('bookstore/v1/', include('product.urls')),
    path('bookstore/v2/', include('product.urls')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('update_server/', views.update, name='update'),
    path('hello/', views.hello_world, name='hello_world'),
    path('', views.home, name='home'),
]

# Configuração adicional para exibir o debug_toolbar
DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": lambda request: True,
}
