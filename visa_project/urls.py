"""visa_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from visa_app import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePage.as_view(),name="index"),
    path('inner/', views.InnerPage.as_view(),name="inner"),
    path('portfolio/', views.PortfolioPage.as_view(),name="portfolio"),
    path('pricing/', views.PricingPage.as_view(),name="pricing"),
    path('services/', views.ServicesPage.as_view(),name="services"),
    path('team/', views.TeamPage.as_view(),name="team"),
    path('about/', views.AboutPage.as_view(),name="about"),
    path('family/', views.FamilyPage.as_view(),name="family"),
    path('student/', views.StudentPage.as_view(),name="student"),
    path('contact/', views.ContactPage.as_view(),name="contact"),
    path('nominee/', views.Nominee.as_view(),name="nominee"),
    path('express_entry/', views.ExpressEntry.as_view(),name="express_entry"),
    path('care_giver/', views.CareGiver.as_view(),name="care_giver"),
    path('coming_soon/', views.Comingpage.as_view(),name="coming_soon"),
    path('blogs/', views.Blog.as_view(), name="blogs"),
    path('spain_coming_soon/',views.Spain_Comingpage.as_view(),name="spain_coming_soon"),
    path('Denmark_coming_soon/',views.Denmark_Comingpage.as_view(),name="Denmark_coming_soon"),
    path('Italy_coming_soon/',views.Italy_Comingpage.as_view(),name="Italy_coming_soon"),
    path('Greece_coming_soon/',views.Greece_Comingpage.as_view(),name="Greece_comingsoon"),
    path('refresh/', views.refresh, name="refresh"),
    path('policy/',views.policy.as_view(),name="policy"),
    path('terms/',views.terms.as_view(),name="terms"),
    path('generaldisclaimer/',views.general.as_view(),name="general"),
    path('givesit/',views.givesit.as_view(),name="givesit"),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
