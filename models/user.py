from models.base_model import BaseModel
from . import storage


class User(BaseModel):
    """
    class User that inherits from BaseModel
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
        Instantiate an instance
        """
        super().__init__(*args, **kwargs)
