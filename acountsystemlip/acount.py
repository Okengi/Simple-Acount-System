from dataclasses import dataclass

@dataclass
class Acount:
    """
        This class only functions as a dataclass for the collums in the db.
    """
    def __init__(self, username, password, i, pi) -> None:
        self.username = username
        self.password = password
        self.mainImagePath = i
        self.profileImagePath = pi