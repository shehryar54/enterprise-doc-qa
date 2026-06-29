from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Enterprise Doc QA"
    OLLAMA_BASE_URL: str = "http://localhost:11434"
    OLLAMA_MODEL: str = "llama3.2"
    CHROMA_PATH: str = "vectorstore"
    CHUNK_SIZE: int = 500
    CHUNK_OVERLAP: int = 50

settings = Settings()