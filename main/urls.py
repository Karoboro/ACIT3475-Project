from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create/trip/", views.create_trip, name="create_trip"),
    path("edit/trip/<int:trip_id>/", views.edit_trip, name="edit_trip"),
    path("delete/trip/<int:trip_id>", views.delete_trip, name="delete_trip"),
    path("create/day/", views.create_day, name="create_day"),
    path("edit/day/<int:day_id>/", views.edit_day, name="edit_day"),
    path("create/event/", views.create_event, name="create_event"),
    path("edit/event/<int:event_id>/", views.edit_event, name="edit_event"),
    path("delete/event/<int:event_id>", views.delete_event, name="delete_event"),
]
