from fastapi import FastAPI,HTTPException, status
from fastapi.staticfiles import StaticFiles

app = FastAPI(
   title="Rent a Room API",
   description="Book a stay in house or Room",
   version ="1.0.0",
   contact ={"name": "test Enterprise LTD","email": "test@example.com"}
)
apartment = {
      "id": 1,
      "name": "Sunny 2-bedroom apartment",
      "price_per_night": 200,
      "bedrooms": 2,
      "bathrooms": 1.5
}
house = {
         "id": 2,
         "name": "cozy 1.5-bedroom apartment",
         "price_per_night":350,
         "bedrooms": 1.5,
         "bathrooms": 1.5
}
studio =  {
      "id": 3,
      "name": "Sunny 2-bedroom apartment",
      "price_per_night": 100,
      "bedrooms": 1,
      "bathrooms": 1
}

@app.get("/",status_code=status.HTTP_200_OK)
def root():
   return {"message": "Welcome to Rent a rooms"}
# "" in room  -> true
# "" in studio -> True
# ""
@app.get("/rooms",status_code=status.HTTP_200_OK)
def get_rooms(max_price: int | None= None, search: str| None = None):
  results = [apartment,house,studio]
  if max_price:
     results = [room for room in results if room["price_per_night"]<=max_price]
  if search:
     results = [room for room in results if search.lower() in room["name"].lower()]
     return results     
@app.get("/rooms/{room_id}",status_code=status.HTTP_200_OK)
def get_room(room_id: int):
   for room in [apartment,house,studio]:
      if room["id"]  == room_id:
         return room 
   raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Room not found") 


   