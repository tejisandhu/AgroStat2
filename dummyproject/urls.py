"""
URL configuration for dummyproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views

from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path("admin/", admin.site.urls),
    path('footer',views.footer,name="handle_footer"),
    path('',views.index, name="index"),
    path('contactus',views.contactus, name="contactus"),
    path('login',views.login,name="login"),
    path('navbar',views.navbar),
    path('registration',views.registration,name="registration"),
    path('base',views.base),
    path('base2',views.base2),
    path('Agri_call_center',views.Agri_call_center,name="Agri_call_center"),
    path('Agri_crops',views.Agri_crops,name="Agri_crops"),
    path('Agri_farmer_scheme',views.Agri_farmer_scheme,name="Agri_farmer_scheme"),
    path('Agri_indian_uni',views.Agri_indian_uni,name="Agri_indian_uni"),
    path('Agri_latest_technology',views.Agri_latest_technology,name="Agri_latest_technology"),
    path('Agri_news',views.Agri_news,name="Agri_news"),
    path('Agri_uni',views.Agri_uni,name="Agri_uni"),
    path('Agri_videos',views.Agri_videos,name="Agri_videos"),
    path('Agri_dealers',views.Agri_dealers,name="Agri_dealers"),
    path('review',views.review,name="review"),
    path('sidebar',views.sidebar,name="sidebar"),
    path('sidebar11',views.sidebar11,name="sidebar11"),
    path('change_password',views.change_password,name="change_password"),
    path('help_support',views.help_support,name="help_support"),
    path('userprofile_s',views.userprofile,name="userprofile_s"),
    path('edit_profile_s',views.edit_profile_s,name="edit_profile_s"),
    path('forget',views.forget,name="forget"),
    path('logout',views.logout,name="logout"),
    path('crop_detail/<str:name>',views.crop_detail,name="crop_detail"),
    path('crop_detail2/<str:name>',views.crop_detail2,name="crop_detail2"),
    path('news_detail/<str:name>',views.news_detail,name="news_detail"),
    path('live',views.live,name="live"),
    path('e503',views.e503,name="e503"),
    path('disease_detection',views.disease_detection,name="disease_detection"),
    path('fertilizer_detection',views.fertilizer_detection,name="fertilizer_detection"),
    path('predict_crop_rice',views.predict_crop_rice,name="predict_crop_rice"),
    path('predict_crop_maize',views.predict_crop_maize,name="predict_crop_maize"),
    path('predict_population',views.predict_population,name="predict_population"),
    path('predict_crop_wheat',views.predict_crop_wheat,name="predict_crop_wheat"),
    path('predict_phosphorous',views.predict_phosphorous,name="predict_phosphorous"),
    path('predict_potassium',views.predict_potassium,name="predict_potassium"),
    path('register_otp',views.register_otp,name="register_otp"),
    path('predict_fruit',views.predict_fruit,name="predict_fruit"),
    path('f1',views.f1,name="f1"),
    path('f2',views.f2,name="f2"),
    path('f3',views.f3,name="f3"),
    path('f4',views.f4,name="f4"),
    path('f5',views.f5,name="f5"),
    path('f6',views.f6,name="f6"),
    path('f7',views.f7,name="f7"),
    path('f8',views.f8,name="f8"),
    path('dashboard',views.dashboard,name="dashboard"),
    path('chat/',views.chat,name="chat"),
    path('chat1/',views.chat1,name="chat1"),
    path('fertilizer_link/',views.fertilizer_link,name="fertilizer_link"),
    path('phosphorous_link/',views.phosphorous_link,name="phosphorous_link"),
    path('potassium_link/',views.potassium_link,name="potassium_link"),
    path('rice_link/',views.rice_link,name="rice_link"),
    path('maize_link/',views.maize_link,name="maize_link"),
    path('wheat_link/',views.wheat_link,name="wheat_link"),
    path('population_link/',views.population_link,name="population_link"),
    path('rice1',views.rice1,name="rice1"),
    path('rice2',views.rice2,name="rice2"),
    path('rice3',views.rice3,name="rice3"),
    path('rice4',views.rice4,name="rice4"),
    path('rice5',views.rice5,name="rice5"),
    path('rice6',views.rice6,name="rice6"),
    path('rice7',views.rice7,name="rice7"),
    path('rice8',views.rice8,name="rice8"),
    
    
    path('maize1',views.maize1,name="maize1"),
    path('maize2',views.maize2,name="maize2"),
    path('maize3',views.maize3,name="maize3"),
    path('maize4',views.maize4,name="maize4"),
    path('maize5',views.maize5,name="maize5"),
    path('maize6',views.maize6,name="maize6"),
    path('maize7',views.maize7,name="maize7"),
    path('maize8',views.maize8,name="maize8"),    
    path('wheat1',views.wheat1,name="wheat1"),
    path('wheat2',views.wheat2,name="wheat2"),
    path('wheat3',views.wheat3,name="wheat3"),
    path('wheat4',views.wheat4,name="wheat4"),
    path('wheat5',views.wheat5,name="wheat5"),
    path('wheat6',views.wheat6,name="wheat6"),
    path('wheat7',views.wheat7,name="wheat7"),
    path('wheat8',views.wheat8,name="wheat8"), 
    path('population1',views.population1,name="population1"),
    path('population2',views.population2,name="population2"),
    path('population3',views.population3,name="population3"),
    path('population4',views.population4,name="population4"),
    path('population5',views.population5,name="population5"),
    path('population6',views.population6,name="population6"),
    path('population7',views.population7,name="population7"),
    path('population8',views.population8,name="population8"),
    path('crops_production_analysis/',views.crops_production_analysis,name="crops_production_analysis"),
    path('crops_production_prediction/',views.crops_production_prediction,name="crops_production_prediction"),
    path('fertilizers_use_analysis/',views.fertilizers_use_analysis,name="fertilizers_use_analysis"),
    path('fertilizers_use_prediction/',views.fertilizers_use_prediction,name="fertilizers_use_prediction"),

    path('phosphorous1',views.phosphorous1,name="phosphorous1"),
    path('phosphorous2',views.phosphorous2,name="phosphorous2"),
    path('phosphorous3',views.phosphorous3,name="phosphorous3"),
    path('phosphorous4',views.phosphorous4,name="phosphorous4"),
    path('phosphorous5',views.phosphorous5,name="phosphorous5"),
    path('phosphorous6',views.phosphorous6,name="phosphorous6"),
    path('phosphorous7',views.phosphorous7,name="phosphorous7"),
    path('phosphorous8',views.phosphorous8,name="phosphorous8"),

    path('potassium1',views.potassium1,name="potassium1"),
    path('potassium2',views.potassium2,name="potassium2"),
    path('potassium3',views.potassium3,name="potassium3"),
    path('potassium4',views.potassium4,name="potassium4"),
    path('potassium5',views.potassium5,name="potassium5"),
    path('potassium6',views.potassium6,name="potassium6"),
    path('potassium7',views.potassium7,name="potassium7"),
    path('potassium8',views.potassium8,name="potassium8"),

    
  
    
]

urlpatterns+=staticfiles_urlpatterns()
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
