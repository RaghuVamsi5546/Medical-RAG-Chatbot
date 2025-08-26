from langchain_groq import ChatGroq
from app.common.logger import get_logger
from app.common.exception import CustomException
from app.config.config import GROQ_API_KEY, GROQ_MODEL_NAME

logger = get_logger(__name__)

def load_llm():
    try:
        if not GROQ_API_KEY:
            raise CustomException(
                "GROQ_API_KEY is not set. Please add GROQ_API_KEY in .env"
            )
        
        logger.info("Loading Conversational LLM from Groq")

        llm = ChatGroq(
            api_key=GROQ_API_KEY,
            model=GROQ_MODEL_NAME,
            temperature=0.7,          
            max_tokens=512         
        )

        logger.info("LLM loaded successfully")
        return llm

    except Exception as e:
        raise CustomException("Failed to load LLM", e)
