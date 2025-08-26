import os
from langchain_community.vectorstores import FAISS
from app.components.embeddings import get_embedding_model
from app.common.logger import get_logger
from app.common.exception import CustomException
from app.config.config import DB_FAISS_PATH

logger = get_logger(__name__)

def load_vector_store():
    try:
        embedding_model = get_embedding_model()
        if os.path.exists(DB_FAISS_PATH):
            logger.info("Loading existing VectorStore")
            return FAISS.load_local(
                DB_FAISS_PATH,
                embedding_model,
                allow_dangerous_deserialization=True
            )
        return None
    except Exception as e:
        raise CustomException("Failed to load VectorStore", e)

def save_vector_store(text_chunks):
    try:
        if not text_chunks:
            raise CustomException("No chunks were provided for VectorStore creation")

        logger.info("Generating new VectorStore")
        embedding_model = get_embedding_model()
        db = FAISS.from_documents(text_chunks, embedding_model)
        db.save_local(DB_FAISS_PATH)
        logger.info("VectorStore saved successfully")
        return db
    except Exception as e:
        raise CustomException("Failed to create VectorStore", e)
