from django.urls import path

from cinema import views

urlpatterns = [
    path("genres/", views.GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", views.GenreDetail.as_view(), name="genre-detail"),
    path("actors/", views.ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", views.ActorDetail.as_view(), name="actor-detail"),
    path(
        "cinema_halls/",
        views.CinemaHallList.as_view(),
        name="cinema-hall-list"
    ),
    path(
        "cinema_halls/<int:pk>/",
        views.CinemaHallDetail.as_view(),
        name="cinema-hall-detail"
    ),
    path("movies/", views.MovieList.as_view(), name="movie-list"),
    path("movies/<int:pk>/", views.MovieDetail.as_view(), name="movie-detail"),
    path(
        "movie_sessions/",
        views.MovieSessionList.as_view(),
        name="movie-session-list"
    ),
    path(
        "movie_sessions/<int:pk>/",
        views.MovieSessionDetail.as_view(),
        name="movie-session-detail"
    ),
]
