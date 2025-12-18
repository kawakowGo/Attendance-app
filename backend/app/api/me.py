from fastapi import APIRouter

router=APIRouter()

@router.get("/me")
def get_me():
    return{
        "id":1,
        "name":"Dummy User",
        "role":"employee"
    }