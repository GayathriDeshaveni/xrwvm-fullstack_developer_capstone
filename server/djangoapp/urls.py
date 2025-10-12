# Uncomment the imports before you add the code
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
from . import views

app_name = 'djangoapp'

urlpatterns = [
    # path for login API (POST request)
    path('login', views.login_user, name='login'),

    # path for logout
    path('logout', views.logout_request, name='logout'),

    # path for registration API (POST request)
    path('registration', views.registration, name='registration'),

    # path for home/index page
    path('', TemplateView.as_view(template_name="index.html"), name='index'),

    # path for dealer listings
    path('dealerships', views.get_dealerships, name='get_dealerships'),

    # path for viewing dealer details
    path('dealer/<int:dealer_id>/', views.get_dealer_details, name='get_dealer_details'),

    # path for viewing dealer reviews
    path('dealer/<int:dealer_id>/reviews/', views.get_dealer_reviews, name='get_dealer_reviews'),

    # path for adding a review
    path('add_review', views.add_review, name='add_review'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
