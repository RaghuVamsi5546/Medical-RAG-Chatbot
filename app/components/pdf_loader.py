import os
from app.common.logger import get_logger
from app.common.exception import CustomException
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from app.config.config import DATA_PATH, CHUNK_SIZE, CHUNK_OVERLAP

logger = get_logger(__name__)

def load_pdf_files():
    try:
        if not os.path.exists(DATA_PATH):
            raise CustomException(f"Data path '{DATA_PATH}' does not exist")

        logger.info(f"Loading PDF files from {DATA_PATH}")

        loader = DirectoryLoader(
            DATA_PATH,
            glob="**/*.pdf",
            loader_cls=PyPDFLoader,
            recursive=True
        )
        documents = loader.load()

        if documents:
            logger.info(f"Successfully loaded {len(documents)} documents")
            logger.debug(
                f"Example files: {[doc.metadata.get('source') for doc in documents[:3]]}"
            )
        else:
            logger.warning("No PDFs found in the directory")

        return documents

    except Exception as e:
        raise CustomException("Error while loading PDF files", e)


def create_text_chunks(documents):
    try:
        if not documents:
            raise CustomException("No documents provided for chunking")

        logger.info(f"Splitting {len(documents)} documents into chunks")

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=CHUNK_SIZE,
            chunk_overlap=CHUNK_OVERLAP
        )
        text_chunks = text_splitter.split_documents(documents)

        logger.info(f"Generated {len(text_chunks)} text chunks")
        return text_chunks

    except Exception as e:
        raise CustomException("Error while creating text chunks", e)
