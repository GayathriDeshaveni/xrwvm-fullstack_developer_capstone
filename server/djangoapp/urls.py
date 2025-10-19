# server/djangoapp/urls.py
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
from . import views

app_name = 'djangoapp'

urlpatterns = [
    path('login', views.login_user, name='login'),
    path('logout', views.logout_request, name='logout'),
    path('registration', views.registration, name='registration'),
    path('get_dealers/', views.get_dealerships, name='get_dealers'),
    path('get_dealers/<str:state>', views.get_dealerships, name='get_dealers_by_state'),
    path('reviews/dealer/<int:dealer_id>', views.get_dealer_reviews, name='dealer_details'),
    path('add_review', views.add_review, name='add_review'),
    path(route='get_cars', view=views.get_cars, name ='getcars'),
    # Frontend React page serving
    path('login/', TemplateView.as_view(template_name="index.html"), name='frontend_login'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
