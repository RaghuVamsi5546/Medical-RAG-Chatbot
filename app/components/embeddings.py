import os
from app.common.logger import get_logger
from app.common.exception import CustomException
from langchain_huggingface import HuggingFaceEmbeddings
from app.config.config import HF_TOKEN

logger = get_logger(__name__)


def get_embedding_model():
    try:
        logger.info("Initializing HuggingFace Embeddings Model (MedEmbed-base-v0.1)")

        embeddings = HuggingFaceEmbeddings(model_name="abhinand/MedEmbed-base-v0.1")

        logger.info("HuggingFace Embedding Model loaded successfully")
        return embeddings

    except Exception as e:
        raise CustomException("Error occurred while loading embedding model", e)

