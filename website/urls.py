from django.urls import path
from .views import admin_page
from .import views



from django.contrib import admin




urlpatterns = [

    path('admin/', admin.site.urls),
    
    path('', views.home, name="home"),
    path('contact.html', views.contact, name="contact"),
    path('about.html', views.about, name="about"),
    path('bookservice.html', views.bookservice, name="bookservice"),
    path('survey.html', views.survey, name="survey"),
    path('shop.html', views.shop, name="shop"),
    path('service.html', views.service, name="service"),
    path('pricing.html', views.pricing, name="pricing"),
    path('appointment.html', views.appointment, name="appointment"),
    path('booknow.html', views.booknow, name="booknow"),
    path('logout.html', views.logout, name="logout"),
    path('login.html', views.login, name="login"),
    path('view.html', views.view, name="view"),
    path('viewcart.html', views.viewcart, name="viewcart"),
    path('admin_page.html', admin_page, name='admin_page'),
    path('status.html', views.status, name='status'),
   




   ]
