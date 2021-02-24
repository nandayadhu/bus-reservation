from django.urls import path
from . import views
from myapp import md_views

urlpatterns = [
    path('', views.home, name="home"),
    path('findbus', views.findbus, name="findbus"),
    path('bookings', views.bookings, name="bookings"),
    path('cancellings', views.cancellings, name="cancellings"),
    path('seebookings', views.seebookings, name="seebookings"),
    path('about/', views.about, name='about'),
    path('success', views.success, name="success"),
    # path('signout', views.signout, name="signout"),

    path('admin_login', md_views.admin_login, name="admin_login"),
    path('admin_home', md_views.admin_home, name="admin_home"),
    path('add_bus', md_views.add_bus, name="add_bus"),
    path('admin_logout', md_views.admin_logout, name="admin_logout"),
    path('book_seat/<str:id>', views.book_seat, name="book_seat"),


    


]
