from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from api.views.auth import LoginApiView, ProfileView
from api.views.level import QuestionView, InputAnswerView, LeaderboardView, CurrentLevelView

urlpatterns = [
    path("login", LoginApiView.as_view(), name="deduce-login"),
    path("refresh", TokenRefreshView.as_view(), name="deduce-token-refresh"),
    path("question", QuestionView.as_view(), name="deduce-question"),
    path("answer", InputAnswerView.as_view(), name="deduce-answer"),
    path("leaderboard", LeaderboardView.as_view(), name="deduce-leaderboard"),
    path("current_level", CurrentLevelView.as_view(), name="deduce-currlevel"),
    path("user_info", ProfileView.as_view(), name="deduce-user-info"),
]
