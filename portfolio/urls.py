# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('about/', views.about, name='about'),
#     path('projects/', views.projects, name='projects'),
#     path('contact/', views.contact, name='contact'),
# ]




from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # path('skills/', views.skills, name='skills'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
    path('contact/submit/', views.contact, name='contact_submit'),  # This is the new path for form submission
]
