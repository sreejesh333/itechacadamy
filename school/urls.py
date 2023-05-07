from django.urls import path
from searchschll.settings import DEBUG,STATIC_URL,STATIC_ROOT,MEDIA_URL,MEDIA_ROOT
from django.conf.urls.static import static
from . import views
app_name = 'school'
urlpatterns = [
     # path('', views.startcontact,name='startcontact'),
     path('', views.index,name='index'),
     path('contact/', views.contact,name='contact'),
     path('abc/', views.abc,name='abc'),
     path('advanced/', views.advanced,name='advanced'),
     # path('diploma/', views.diploma,name='diploma'),
     # path('online/', views.online,name='online'),
     # path('view/', views.view,name='view'),
     
     
    
    
]



if DEBUG:
    urlpatterns += static(STATIC_URL,document_root=STATIC_ROOT)
    urlpatterns += static(MEDIA_URL,document_root=MEDIA_ROOT)