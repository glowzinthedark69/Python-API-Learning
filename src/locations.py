import random
from typing import List, Optional
from fastapi import HTTPException, Body, Path
from pydantic import BaseModel, validator
from app import app

locations = []


class Location(BaseModel):
    id: Optional[int] = None
    city: Optional[str] = None
    country: Optional[str] = None

    @validator('city', 'country')
    def check_name(cls, value):
        if not value:
            raise ValueError('city and country cannot be empty')
        return value


@app.post("/locations", response_model=Location, status_code=201)
def create_location(location: Location = Body(...)):
    location.id = random.randint(10000, 99999)  # generate a random 5-digit number
    locations.append(location)
    return location


@app.get("/locations", response_model=List[Location])
def get_locations():
    return locations


@app.get("/locations/{location_id}", response_model=Location)
def get_location(location_id: int = Path(..., ge=0)):
    for location in locations:
        if location.id == location_id:
            return location
    raise HTTPException(status_code=404, detail="Location not found")


@app.put("/locations/{location_id}", response_model=Location)
def update_location(location_id: int, location: Location = Body(...)):
    for l in locations:
        if l.id == location_id:
            l.city = location.city
            l.country = location.country
            return l
    raise HTTPException(status_code=404, detail="Location not found")


@app.patch("/locations/{location_id}", response_model=Location)
def patch_location(location_id: int, location: Location = Body(...)):
    for l in locations:
        if l.id == location_id:
            if location.city is not None:
                l.city = location.city
            if location.country is not None:
                l.country = location.country
            return l
    raise HTTPException(status_code=404, detail="Location not found")


@app.delete("/locations/{location_id}")
def delete_location(location_id: int):
    for location in locations:
        if location.id == location_id:
            locations.remove(location)
            return {"message": "Location has been successfully deleted."}
    raise HTTPException(status_code=404, detail="Location not found")
