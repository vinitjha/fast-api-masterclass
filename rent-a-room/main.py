from fastapi import FastAPI, status

app = FastAPI(title="Rent a Room API",description="Book a stay in house or Room")
@app.get("/",status_code=status.HTTP_200_OK)
def root():
   
   return {"message": "Welcome to Rent a rooms"}
