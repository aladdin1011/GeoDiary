from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
import os
from supabase import create_client, Client

# Загрузка переменных окружения из .env файла
load_dotenv()

# Получение URL и ключа Supabase из переменных окружения
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")

# Создание клиента Supabase
supabase: Client = create_client(url, key)

app = FastAPI()

# Настройка CORS
origins = [
    "http://localhost:4321",  # Добавьте сюда ваш фронтенд URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SignInData(BaseModel):
    email: str
    password: str

@app.post("/auth/signin")
async def sign_in(data: SignInData):
    try:
        print(f"Received sign-in request for email: {data.email}")
        response = supabase.auth.sign_in_with_password({"email": data.email, "password": data.password})
        print(f"Supabase response: {response}")
        if response.user is None:
            raise HTTPException(status_code=400, detail=response["error"]["message"])
        return {"message": "Sign in successful", "data": response}
    except Exception as e:
        print(f"Error during sign-in: {e}")
        raise HTTPException(status_code=400, detail=str(e))

