from entities.user import User
from repositories.user_repository import (
    user_repository as default_user_repository
)


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository=default_user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password, password_confirmation):
        self.validate(username, password, password_confirmation)

        if not username.isalpha():
            raise UserInputError("Username should only contain letters a-z")

        if len(username) < 3:
            raise UserInputError("Username length should be at least 3.")
        
        if self._user_repository.find_by_username(username) != None:
            raise UserInputError("Username is already taken.")
        
        if len(password) < 8:
            raise UserInputError("Password length should be at least 8.")

        if password.isalpha():
            raise UserInputError("Password should contain characters different from a-z")

        if password != password_confirmation:
            raise UserInputError("Passwords do not match")
        
        

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password, password_confirmation):
        if not username or not password:
            raise UserInputError("Username and password are required")

        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa


user_service = UserService()
