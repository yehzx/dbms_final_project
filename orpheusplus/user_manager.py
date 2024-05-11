import json

from orpheusplus import USER_PATH


class UserManager():
    def __init__(self):
        self.info = self.load_user()
    
    def load_user(self):
        # Load from .meta/user
        try:
            with open(USER_PATH, "r") as f:
                user = json.load(f)
        except:
            self._handle_user_not_exist()

        return user

    @staticmethod 
    def save_user(database, user, passwd):
        # Save to .meta/user
        with open(USER_PATH, "w") as f:
            json.dump({"database": database, "user": user,
                       "passwd": passwd}, f)
    
    def _handle_user_not_exist(self):
        raise Exception("User not exist. Please run `orpheusplus config`.")
