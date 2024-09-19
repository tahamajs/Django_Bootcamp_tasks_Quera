from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import *

app_name = "pineapple"

urlpatterns = [
    path('subscription/create/', subscription_create_view, name='subscription-create'),
    path('subscription/list/', subscription_list_view, name='subscription-list'),
    path('seller/list/', seller_list_view, name='seller-list'),
    path('seller/detail/<str:certificate_code>/', seller_detail_view, name='seller-detail'),
    path('seller/create/', seller_create_view, name='seller-create'),
    path('seller/update/<str:certificate_code>/', seller_update_view, name='seller-update'),
    path('pineapple/list/', pineapple_list_view, name='pineapple-list'),
    path('pineapple/detail/<int:pk>', pineapple_detail_view, name='pineapple-detail'),
    path('pineapple/create/', pineapple_create_view, name='pineapple-create'),
    path('pineapple/update/<int:pk>/', pineapple_update_view, name='pineapple-update'),
    path('seller/pineapple/list/<int:seller_id>/', seller_pineapple_list_view, name='seller-pineapple-list'),
    path('order/list/', order_list_view, name='order-list'),
    path('order/detail/<int:pk>/', order_detail_view, name='order-detail'),
    path('order/create/', order_create_view, name='order-create'),
    path('order/update/<int:pk>/', order_update_view, name='order-update'),
    path('comment/create/', comment_create_view, name='comment-create'),
    path('seller/comment/list/<str:certificate_code>/', seller_comment_list_view, name='seller-comment-list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)