from langchain_openai import ChatOpenAI
import os

class LLM:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.model = ChatOpenAI(model="gpt-4o-mini", api_key=self.api_key)

    def generate_answer(self, question: str, snippets: list) -> str:
        """Generates an answer using an LLM."""
        prompt = f"Context: Use the following paragraphs:\n{snippets}\n Answer the following question: {question}\n with a concise answer, if you don't know the answer just say i don't know"
        answer = self.model.invoke(prompt)

        return answer.content