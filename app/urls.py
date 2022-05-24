
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('service/',views.service,name='service'),
    path('blogs/',views.blogs,name='blogs'),
    path('blog_left_detail/',views.blog_left_details,name='blog_left_detail'),
    path('blog_detail/',views.blog_detail,name='blog_detail'),
    path('appointment/',views.appointment,name='appointment'),
    path('shop/',views.shop,name='shop'),
    path('shop_single/',views.shop_single,name='shop_single'),
    path('cart/',views.cart,name='cart'),
    path('checkout/',views.checkout,name='checkout'),
    path('astrologer/',views.astrologer,name='astrologer'),
    path('privacy_policy/',views.privacy_policy,name='privacy_policy'),
    path('error/',views.error,name='error'),
    path('faq/',views.faq,name='faq'),
    path('contact/',views.contact,name='contact'),
    
]
