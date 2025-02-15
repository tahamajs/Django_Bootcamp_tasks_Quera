from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from .views import views_pineapple , views_subscription , views_orders , views_sellers , views_comments

app_name = "pineapple"

urlpatterns = [

    path("subscription-create" , views_subscription.subscription_create_view ,name = "subscription-create"),
    path("subscription-list" , views_subscription.subscription_list_view , name = "subscription-list"),
    path("seller_list",views_sellers.seller_list_view,name="seller-list"),
    path("seller-detail/<int:seller_id>/",views_sellers.seller_detail_view,name="seller-detail"),
    path("seller-create",views_sellers.seller_create_view,name="seller-create"),
    path("seller-update/<int:pk>/",views_sellers.seller_update_view,name="seller-update"),

    path("pineapple-list",views_pineapple.pineapple_list_view,name = "pineapple-list"),
    path("pineapple-detail/<int:pk>/",views_pineapple.pineapple_detail_view,name="pineapple-detail"),
    path("pineapple-create",views_pineapple.pineapple_create_view,name="pineapple-create"),
    path("pineapple-update/<int:pk>/",views_pineapple.pineapple_update_view,name="pineapple-update"),
    path("seller-pineapple-list/<int:seller_id>/",views_pineapple.seller_pineapple_list_view,name="seller-pineapple-list"),

    path("order-list",views_orders.order_list_view,name = "order-list"),
    path("order-detail/<int:pk>/",views_orders.order_detail_view,name = "order-detail"),
    path("order-create",views_orders.order_create_view,name="order-create"),
    path("order-update/<int:pk>/",views_orders.order_update_view,name="order-update"),

    path("comment-create" ,views_comments.comment_create_view,name="comment-create"),
    path("seller-comment-list/<str:certificate_code>/",views_comments.seller_comment_list_view,name="seller-comment-list"),





    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)