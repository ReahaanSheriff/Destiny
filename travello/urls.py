from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('bookForm/<int:id>',views.bookForm,name='bookForm'),
    path('book/<int:did>',views.book,name='book'),
    path('myBookings/',views.myBookings,name='myBookings'),
]