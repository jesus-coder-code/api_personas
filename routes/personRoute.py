from fastapi import APIRouter
 
router = APIRouter()

@router.get("/HelloWorld")
async def root():
    return [{"message": "Hello World"}]

@router.get("/getPerson")
async def get():
    return [{"message":"this is to get all records"}]

@router.post("/createPerson")
async def create():
    return [{"message":"this is to create new record"}]