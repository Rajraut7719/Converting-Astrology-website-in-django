from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'app/index.html')

def about(request):
    return render(request,'app/about.html')

def service(request):
    return render(request,'app/service.html')

def blogs(request):
    return render(request,'app/blogs/blog.html')

def blog_left_details(request):
    return render(request,'app/blogs/blog_left_detail.html')

def blog_detail(request):
    return render(request,'app/blogs/blog_detail.html')

def appointment(request):
    return render(request,'app/appointment.html')

def shop(request):
    return render(request,'app/shop/shop.html')

def shop_single(request):
    return render(request,'app/shop/shop_single.html')

def cart(request):
    return render(request,'app/shop/cart.html')

def checkout(request):
    return render(request,'app/shop/checkout.html')

def astrologer(request):
    return render(request,'app/pages/astrologer.html')

def privacy_policy(request):
    return render(request,'app/pages/privacy_policy.html')

def error(request):
    return render(request,'app/pages/error.html')

def faq(request):
    return render(request,'app/pages/faq.html')

def contact(request):
    return render(request,'app/contact/contact.html')
