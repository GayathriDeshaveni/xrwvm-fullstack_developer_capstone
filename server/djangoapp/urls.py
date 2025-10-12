from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
from . import views

app_name = 'djangoapp'

urlpatterns = [
    # API endpoints
    path('login', views.login_user, name='login'),
    path('logout', views.logout_request, name='logout'),
    path('registration', views.registration, name='registration'),
    path('dealerships', views.get_dealerships, name='get_dealerships'),
    path('dealer/<int:dealer_id>/', views.get_dealer_details, name='get_dealer_details'),
    path('dealer/<int:dealer_id>/reviews/', views.get_dealer_reviews, name='get_dealer_reviews'),
    path('add_review', views.add_review, name='add_review'),

    # 👇 Add this AFTER all API routes
    # This serves your React page for the frontend route /login
    path('login/', TemplateView.as_view(template_name="index.html"), name='frontend_login'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
