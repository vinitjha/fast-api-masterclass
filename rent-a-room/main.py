from fastapi import FastAPI, status

app = FastAPI()
@app.get("/",status_code=status.HTTP_103_EARLY_HINTS)
def root():
   return {"message": "Welcome to Rent a rooms"}
