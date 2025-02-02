from fastapi import FastAPI
from pydantic import BaseModel
from app.embeddings import Embeddings
from app.model_integration import LLM

app = FastAPI()
embeddings = Embeddings()
llm = LLM()

class Query(BaseModel):
    question: str


@app.post("/ask")
async def answer_question(query: Query):
    snippets = embeddings.get_relevant_snippets(query.question)
    answer = llm.generate_answer(query.question, snippets)
    return {"answer": answer, "snippets": snippets}