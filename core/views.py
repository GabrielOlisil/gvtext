# Create your views here.


from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import UserSerializer


class HomeView(APIView):
    def get(self, request):
        return Response({"up_status": "up"})


class UserView(APIView):
    def get(self, request):
        users = User.objects.all()
        return Response([UserSerializer.to_json(user) for user in users])

    def post(self, request):
        datareq = request.data
        user = User(name=datareq["name"], age=datareq["age"])
        user.save()
        return Response(UserSerializer.to_json(user))
