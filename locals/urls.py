from django.urls import path

from .views import (HomePageView,
                    # local views
                    LocalsListView, UpdateLocalView, CreateLocalView,
                    local_detail_view,
                    # member vies
                    MemberListView,
                    MemberDetailView,
                    add_member_view,
                    update_member_view,
                    search_view,
                    ExecutiveListView,
                    )

app_name = "locals"

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('locals/', LocalsListView.as_view(), name="locals-list"),
    path('locals/add/', CreateLocalView.as_view(), name="locals-add"),
    path('locals/<int:pk>/', local_detail_view, name="locals-detail"),
    path('locals/<int:pk>/update/',
         UpdateLocalView.as_view(),
         name="locals-edit"),
    path('locals/<int:pk>/members/add', add_member_view, name="members-add"),
    path('members/<int:pk>/edit',
         update_member_view,
         name="members-edit"),
    path('members/', MemberListView.as_view(), name="members-list"),
    path('members/<int:pk>', MemberDetailView.as_view(), name="members-detail"),
    path('executives/', ExecutiveListView.as_view(), name="executives-list"),
    path('search/', search_view, name="search")
]