from django.urls import path
from .views import HomePageView, AboutUsView, ContactUsView, TeamPageView, archives_home_view_media
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('',HomePageView.as_view(), name = 'home'),
    path('archivesHome/',archives_home_view_media, name = 'archivesHome'),
    path('about/',AboutUsView.as_view(), name = 'about'),
    path('contact/',ContactUsView.as_view(), name = 'contact'  ),
    path('team/', TeamPageView.as_view(), name = 'team'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)