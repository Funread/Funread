from UserBadge import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('api/user-badges/', views.award_badge_to_user),
    path('api/user-badges/<int:user_id>/', views.list_user_badges),
    path('api/user-badges/<int:user_badge_id>/', views.delete_user_badge),
     
]

urlpatterns = format_suffix_patterns(urlpatterns)



