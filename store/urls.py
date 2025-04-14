from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('puppies/', views.puppies, name='puppies'),
    path('puppy/<int:pk>/', views.puppy_detail, name='puppy_detail'),
    path('adopt/<int:pk>/', views.adopt, name='adopt'),
    path('thank-you/', views.thank_you, name='thank_you'),
    path('contact/', views.contact, name='contact'),
    path('puppies/search/', views.puppy_search, name='puppy_search'),
    path('adoption-agreement/', views.adoption_agreement, name='adoption_agreement'),
]

