from django.urls import path
from.views import UserQuery, AdminUpdate, UserQueryStatus,GetUserQuery

urlpatterns = [
    path("user_query",UserQuery.as_view()),
    path("update",AdminUpdate.as_view()),
    path("status_request",UserQueryStatus.as_view()),
    path("fetch_users",GetUserQuery.as_view()),
] 