import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()


@dataclass
class Settings:
    openai_api_key: str | None = os.getenv("OPENAI_API_KEY")
    aws_region: str = os.getenv("AWS_REGION", "us-east-1")
    bedrock_model_id: str | None = os.getenv("BEDROCK_MODEL_ID")
    vertex_ai_project: str | None = os.getenv("VERTEX_AI_PROJECT")
    llama_model_path: str | None = os.getenv("LLAMA_MODEL_PATH")


settings = Settings()
