""" User schemas"""
# On va pas trop l'utiliser dans notre cas 
from pydantic import BaseModel, EmailStr

class UserBase(BaseModel): 
    username: str
    email: EmailStr
    full_name: str | None = None

# On fait hériter les classes de la première  car on veut format username...
class UserIn(UserBase): 
    """Base schema for user data."""

    password: str

class UserUpdate(UserBase): 
    "Schema for modifiying user data "
    username: str | None = None
    email: EmailStr | None = None
    password: str | None = None
    full_name: str | None = None



class UserOut(UserBase):
    "Schema for user output data" 
    id:int
    