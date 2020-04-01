from flask import request, jsonify, Response
from flask.views import MethodView

from .models import User


class UserService(MethodView):
    def __init__(self, session_factory, logger):
        self._session_factory = session_factory
        self.logger = logger

    def get(self, user_id):
        if user_id is None:
            return self.list()

        session = self._session_factory()
        user = session.query(User).filter(User.id == user_id).one_or_none()

        if user is None:
            return Response("", status=404)

        return jsonify({"id": user.id, "name": user.name})

    def post(self):
        session = self._session_factory()

        new_user = User(name=request.json["name"])

        session.add(new_user)
        session.commit()
        session.refresh(new_user)

        return jsonify({"id": new_user.id, "name": new_user.name})

    def delete(self, user_id):
        session = self._session_factory()

        session.query(User).filter(User.id == user_id).delete()
        session.commit()
        return Response("", status=200)

    def patch(self, user_id):
        return Response("", status=501)

    def list(self):
        session = self._session_factory()

        return jsonify([{"id": u.id, "name": u.name} for u in session.query(User)])
