from typing import List, Optional
from fastapi import HTTPException, Body, Path
from pydantic import BaseModel
from app import app

locations = []


class Location(BaseModel):
    id: Optional[int] = None
    city: Optional[str] = None
    country: Optional[str] = None


@app.post("/locations", response_model=Location, status_code=201)
def create_location(location: Location = Body(...)):
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


@app.delete("/locations/{location_id}")
def delete_location(location_id: int):
    for location in locations:
        if location.id == location_id:
            locations.remove(location)
            return {"message": "Location has been successfully deleted."}
    raise HTTPException(status_code=404, detail="Location not found")
