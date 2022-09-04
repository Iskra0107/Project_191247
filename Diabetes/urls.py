from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name="home"),
    path('izmeri/', views.izmeri, name="izmeri"),
    path('education/', views.edu , name="education"),
    path('ishrana/', views.ishrana , name="ishrana"),
    path('vezbi/', views.vezbi, name="vezbi"),
    path('dijabetis/',views.dijabetis , name="dijabetis"),
    path('potsetnik/', views.potsetnik, name="potsetnik"),
]
