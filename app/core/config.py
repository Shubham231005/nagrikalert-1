from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "NagrikAlert"
    # REPLACE WITH YOUR SUPABASE URL
    DATABASE_URL: str = "postgresql://postgres:PASSWORD@db.PROJECT_REF.supabase.co:5432/postgres"

settings = Settings()