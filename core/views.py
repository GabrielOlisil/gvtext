# Create your views here.


from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import UserSerializer


class UserView(APIView):
    def get(self, request):
        users = User.objects.all()
        return Response([UserSerializer.to_json(user) for user in users])

    def post(self, request):
        data = request.data
        user = User(name=data["name"], age=data["age"])
        user.save()
        return Response(UserSerializer.to_json(user))
