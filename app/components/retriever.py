from langchain.chains.retrieval_qa.base import RetrievalQA
from langchain_core.prompts import PromptTemplate
from app.components.vector_store import load_vector_store
from app.components.llm import load_llm
from app.common.logger import get_logger
from app.common.exception import CustomException

logger = get_logger(__name__)

CUSTOM_PROMPT_TEMPLATE = """
You are a helpful and reliable medical assistant. Use the provided context to answer the user's query accurately, 
but if the context is insufficient, say you are unsure instead of making up information.

Context:
{context}

Question:
{question}

Instructions:
- Answer clearly and concisely in simple language.
- If the query is medical, give professional and safe advice.
- Do not provide harmful, speculative, or unsafe recommendations.
- If appropriate, suggest consulting a qualified healthcare professional.

Answer:
"""

def set_custom_prompt():
    return PromptTemplate(
        template=CUSTOM_PROMPT_TEMPLATE,
        input_variables=["context", "question"]
    )

def create_qa_chain():
    try:
        logger.info("Loading vectorstore for context")
        db = load_vector_store()
        if db is None:
            raise CustomException("VectorStore is not present or empty")
        logger.info("VectorStore loaded successfully")

        llm = load_llm()  # Uses ChatGroq internally
        if llm is None:
            raise CustomException("LLM is not present or empty")
        logger.info("LLM loaded successfully")

        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=db.as_retriever(search_kwargs={"k": 1}),
            return_source_documents=False,
            chain_type_kwargs={"prompt": set_custom_prompt()}
        )

        logger.info("Successfully created QA chain")
        return qa_chain

    except Exception as e:
        raise CustomException("Failed to make QA chain", e)
