# Python
from datetime import date, datetime
from typing import List, Optional
from uuid import UUID

# Pydantic
from pydantic import BaseModel, Field, EmailStr

# FastAPI
from fastapi import FastAPI, status

app = FastAPI()


# Models

class UserBase(BaseModel):
    user_id: UUID = Field(
        ...
    )
    email: EmailStr = Field(
        ...
    )
class UserLogin(UserBase):
    """
    User Login

    Model to return when the suer logs in
    """
    password: str = Field(
        ...,
        min_length=8,
        max_length=64
    )

class User(UserBase):
    first_name: str = Field(
        ...,
        min_length=3,
        max_length=50
    )
    last_name: str = Field(
        ...,
        min_length=3,
        max_length=50
    )
    birth_date: Optional[date] = Field(default=None)

    username: str = Field(
        ...
    )


class Tweet(BaseModel):
    tweet_id:UUID = Field(...)
    content:str = Field(
        ...,
        min_length=1,
        max_length=256
    )
    create_at: datetime = Field(default=datetime.now())
    update_at: Optional[datetime] = Field(default=None)
    by: User = Field(...)


# Path Operations

@app.get(path="/")
def home():
    return {"Twitter API": "Working!"}

## Users
### Register a User
@app.post(
    path="/singup",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Register a User",
    tags=["Users"]
)
def singup():
    """
    Sing Up

    Register a User
    """
    pass

### Login a User
@app.post(
    path="/login",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Login a User",
    tags=["Users"]
)
def login():
    pass

### Show all Users
@app.get(
    path="/users",
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary="Show all Users",
    tags=["Users"]
)
def show_all_users():
    pass

### Show a User
@app.get(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Show a User",
    tags=["Users"]
)
def show_a_user():
    pass

### Delete a User
@app.delete(
    path="/users/{user_id}/delete",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="delete a User",
    tags=["Users"]
)
def delete_a_user():
    pass

### Update a User
@app.put(
    path="/users/{user_id}/update",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Update a Users",
    tags=["Users"]
)
def update_a_user():
    pass


## Tweets

### Show all tweets
@app.get(
    path="/",
    response_model=List[Tweet],
    status_code=status.HTTP_200_OK,
    summary="Show all tweets",
    tags=["Tweets"]
)
def home():
    return {"tweets":"Working!!"}

@app.post(
    path="/post",
    response_model=Tweet,
    status_code=status.HTTP_201_CREATED,
    summary="Post a tweet",
    tags=["Tweets"]
)
def post_a_tweet():
    pass

### Show a tweets
@app.get(
    path="/tweets/{tweet_id}",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Show a tweet",
    tags=["Tweets"]
)
def show_a_tweet():
    pass

@app.delete(
    path="/tweets/{tweet_id}/delete",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Delete a tweets",
    tags=["Tweets"]
)
def delete_a_tweet():
    pass

@app.put(
    path="/tweets/{tweet_id}/update",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Update a tweets",
    tags=["Tweets"]
)
def update_a_tweet():
    pass