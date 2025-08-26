import os
from app.components.pdf_loader import load_pdf_files, create_text_chunks
from app.components.vector_store import save_vector_store
from app.common.logger import get_logger
from app.common.exception import CustomException

logger = get_logger(__name__)

def process_and_store_pdfs():
    try:
        logger.info("Making the VectorStore")

        documents = load_pdf_files()
        if not documents:
            logger.warning("No documents to process. Exiting.")
            return

        text_chunks = create_text_chunks(documents)
        if not text_chunks:
            logger.warning("No text chunks to process. Exiting.")
            return

        save_vector_store(text_chunks)
        logger.info("VectorStore created successfully")

    except Exception as e:
        raise CustomException("Failed to create VectorStore", e)

if __name__ == "__main__":
    process_and_store_pdfs()
