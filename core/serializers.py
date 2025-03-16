class UserSerializer:
    @staticmethod
    def to_json(user):
        return {"id": str(user.id), "name": user.name, "age": user.age}
