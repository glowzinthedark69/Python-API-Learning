from typing import List, Optional

from fastapi import FastAPI, HTTPException, Body, Path
from pydantic import BaseModel

app = FastAPI()

users = []


class User(BaseModel):
    userId: int
    name: str
    city: str
    country: str
    jobTitle: str


@app.get("/users", response_model=List[User])
def get_users(name: Optional[str] = None, userId: Optional[int] = None, city: Optional[str] = None,
              country: Optional[str] = None, jobTitle: Optional[str] = None):
    if userId is not None and userId < 0:
        raise HTTPException(status_code=400, detail="userId cannot be a negative number")

    filtered_users = users

    if name is not None:
        filtered_users = [user for user in filtered_users if name.lower() in user.name.lower()]
    if userId is not None:
        filtered_users = [user for user in filtered_users if user.userId == userId]
    if city is not None:
        filtered_users = [user for user in filtered_users if city.lower() in user.city.lower()]
    if country is not None:
        filtered_users = [user for user in filtered_users if country.lower() in user.country.lower()]
    if jobTitle is not None:
        filtered_users = [user for user in filtered_users if jobTitle.lower() in user.jobTitle.lower()]

    return filtered_users


@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int = Path(..., ge=0)):
    for user in users:
        if user.userId == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")


@app.post("/users", response_model=User)
def create_user(user: User = Body(...)):
    for u in users:
        if u.userId == user.userId:
            raise HTTPException(status_code=400, detail="This user already exists. Please verify information.")
    users.append(user)
    return user


@app.patch("/users/{user_id}", response_model=User)
def patch_user(user_id: int, user: User = Body(...)):
    if user.userId != user_id:
        raise HTTPException(status_code=400, detail="User ID in request body does not match URL parameter")
    for u in users:
        if u.userId == user_id:
            u.name = user.name if user.name else u.name
            u.city = user.city if user.city else u.city
            u.country = user.country if user.country else u.country
            u.jobTitle = user.jobTitle if user.jobTitle else u.jobTitle
            return u
    raise HTTPException(status_code=404, detail="User not found")


@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, user: User = Body(...)):
    for u in users:
        if u.userId == user_id:
            u.name = user.name
            u.city = user.city
            u.country = user.country
            u.jobTitle = user.jobTitle
            return u
    raise HTTPException(status_code=404, detail="User not found")


@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    for user in users:
        if user.userId == user_id:
            users.remove(user)
            return {"message": "User has been successfully deleted."}
    raise HTTPException(status_code=404, detail="User not found")
