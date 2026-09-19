from fastapi import FastAPI,HTTPException, status
from fastapi.staticfiles import StaticFiles

app = FastAPI(
   title="Rent a Room API",
   description="Book a stay in house or Room",
   version ="1.0.0",
   contact ={"name": "test Enterprise LTD","email": "test@example.com"}
)

app.mount("/assets",StaticFiles(directory="assets"),name="assets")
apartment = {
      "id": 1,
      "name": "Sunny 2-bedroom apartment",
      "price_pernight": 200,
      "bedrooms": 2,
      "bathrooms": 1.5
}
house = {
         "id": 2,
         "name": "cozy 1.5-bedroom apartment",
         "price_pernight":350,
         "bedrooms": 1.5,
         "bathrooms": 1.5
}
studio =  {
      "id": 3,
      "name": "Sunny 2-bedroom apartment",
      "price_pernight": 100,
      "bedrooms": 1,
      "bathrooms": 1
}
def do_something():
   print("random stuff")
   print("do something")
@app.get("/",status_code=status.HTTP_200_OK)
def root():
   return {"message": "Welcome to Rent a rooms"}
@app.get("/rooms",status_code=status.HTTP_200_OK)
def get_rooms():
   return [apartment,house,studio]
@app.get("/rooms/{room_id}",status_code=status.HTTP_200_OK)
@app.get("/rooms/faq",status_code=status.HTTP_200_OK)
def get_room_faq():
   return {"check_in": "From 3 PM","checkout": "Untill 11AM"} 
def get_room(room_id: int):
   for room in [apartment,house,studio]:
      if room["id"]  == room_id:
         do_something()
         return room 
   raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Room not found") 


   