from django.urls import path

from .views import (HomePageView,
                    LocalsListView,
                    UpdateLocalView,
                    CreateLocalView,
                    local_detail_view,
                    add_member_view)

app_name = "locals"

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('locals/', LocalsListView.as_view(), name="locals-list"),
    path('locals/add/', CreateLocalView.as_view(), name="locals-add"),
    path('locals/<int:pk>/', local_detail_view, name="locals-detail"),
    path('locals/<int:pk>/update/',
         UpdateLocalView.as_view(),
         name="locals-edit"),
    path('locals/<int:pk>/add', add_member_view, name="locals-members-add"),

]