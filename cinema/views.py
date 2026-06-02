from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from cinema.models import Genre, Actor, CinemaHall, Movie, MovieSession
from cinema.serializers import (
    GenreSerializer,
    ActorSerializer,
    CinemaHallSerializer,
    MovieSerializer,
    MovieListSerializer,
    MovieDetailSerializer,
    MovieSessionSerializer,
    MovieSessionListSerializer,
    MovieSessionDetailSerializer,
)


class GenreList(APIView):
    def get(self, request: Request) -> Response:
        serializer = GenreSerializer(Genre.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        serializer = GenreSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class GenreDetail(APIView):
    def get_object(self, pk: int) -> Genre | None:
        try:
            return Genre.objects.get(pk=pk)
        except Genre.DoesNotExist:
            return None

    def get(self, request: Request, pk: int) -> Response:
        genre = self.get_object(pk)
        if genre is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(GenreSerializer(genre).data)

    def put(self, request: Request, pk: int) -> Response:
        genre = self.get_object(pk)
        if genre is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = GenreSerializer(genre, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request: Request, pk: int) -> Response:
        genre = self.get_object(pk)
        if genre is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        genre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ActorList(APIView):
    def get(self, request: Request) -> Response:
        serializer = ActorSerializer(Actor.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request: Request) -> Response:
        serializer = ActorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ActorDetail(APIView):
    def get_object(self, pk: int) -> Actor | None:
        try:
            return Actor.objects.get(pk=pk)
        except Actor.DoesNotExist:
            return None

    def get(self, request: Request, pk: int) -> Response:
        actor = self.get_object(pk)
        if actor is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(ActorSerializer(actor).data)

    def put(self, request: Request, pk: int) -> Response:
        actor = self.get_object(pk)
        if actor is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ActorSerializer(actor, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request: Request, pk: int) -> Response:
        actor = self.get_object(pk)
        if actor is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        actor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CinemaHallList(APIView):
    def get(self, request: Request) -> Response:
        serializer = CinemaHallSerializer(CinemaHall.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request: Request) -> Response:
        serializer = CinemaHallSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CinemaHallDetail(APIView):
    def get_object(self, pk: int) -> CinemaHall | None:
        try:
            return CinemaHall.objects.get(pk=pk)
        except CinemaHall.DoesNotExist:
            return None

    def get(self, request: Request, pk: int) -> Response:
        hall = self.get_object(pk)
        if hall is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(CinemaHallSerializer(hall).data)

    def put(self, request: Request, pk: int) -> Response:
        hall = self.get_object(pk)
        if hall is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CinemaHallSerializer(hall, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request: Request, pk: int) -> Response:
        hall = self.get_object(pk)
        if hall is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        hall.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request: Request, pk: int) -> Response:
        hall = self.get_object(pk)
        if hall is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CinemaHallSerializer(
            hall,
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class MovieList(APIView):
    def get(self, request: Request) -> Response:
        serializer = MovieListSerializer(Movie.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request: Request) -> Response:
        serializer = MovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class MovieDetail(APIView):
    def get_object(self, pk: int) -> Movie | None:
        try:
            return Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return None

    def get(self, request: Request, pk: int) -> Response:
        movie = self.get_object(pk)
        if movie is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(MovieDetailSerializer(movie).data)

    def put(self, request: Request, pk: int) -> Response:
        movie = self.get_object(pk)
        if movie is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = MovieSerializer(movie, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request: Request, pk: int) -> Response:
        movie = self.get_object(pk)
        if movie is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MovieSessionList(APIView):
    def get(self, request: Request) -> Response:
        serializer = MovieSessionListSerializer(
            MovieSession.objects.all(), many=True
        )
        return Response(serializer.data)

    def post(self, request: Request) -> Response:
        serializer = MovieSessionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class MovieSessionDetail(APIView):
    def get_object(self, pk: int) -> MovieSession | None:
        try:
            return MovieSession.objects.get(pk=pk)
        except MovieSession.DoesNotExist:
            return None

    def get(self, request: Request, pk: int) -> Response:
        session = self.get_object(pk)
        if session is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(MovieSessionDetailSerializer(session).data)

    def put(self, request: Request, pk: int) -> Response:
        session = self.get_object(pk)
        if session is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = MovieSessionSerializer(session, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request: Request, pk: int) -> Response:
        session = self.get_object(pk)
        if session is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        session.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
