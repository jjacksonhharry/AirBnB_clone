from models.base_model import BaseModel


class Review(BaseModel):
    """
    class representing reviews
    """
    place_id = ""
    user_id = ""
    text = ""
