from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from main import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('signin/', views.SignInView.as_view(), name='signin'),
    path('signout/', LogoutView.as_view(), name='signout'),
    path('user-home/', views.UserHomeView.as_view(), name='user-home'),
    path('alumnis/', views.AlumniListView.as_view(), name='alumni-list'),
    path('news-add/', views.NewsAddView.as_view(), name='news-add'),
    path('news-update/<int:pk>/', views.NewsUpdateView.as_view(), name='news-update'),
    path('news-list/', views.NewsListView.as_view(), name='news-list'),
    path('event-list/', views.EventListView.as_view(), name='event-list'),
    path('event-add/', views.EventAddView.as_view(), name='event-add'),
    path('event-update/<int:pk>/', views.EventUpdateView.as_view(), name='event-update'),
    path('photo-add/', views.PhotoAddView.as_view(), name='photo-add'),
    path('photo-list/', views.PhotoListView.as_view(), name='photo-list'),
    path('feedback-add/', views.FeedbackAddView.as_view(), name='feedback-add'),
    path('feedback-list/', views.FeedbackListView.as_view(), name='feedback-list'),
    path('response-add/<int:feed_id>/', views.ResponseAddView.as_view(), name='response-add'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)