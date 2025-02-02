from langchain_openai import ChatOpenAI
import os
import openai

class LLM:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            print("ERROR: OPENAI_API_KEY is not set!")
            raise ValueError("OpenAI API Key is missing! Set OPENAI_API_KEY before running.")
        
        self.model = ChatOpenAI(model="gpt-4o-mini", api_key=self.api_key)

        openai.api_key = self.api_key

    def generate_answer(self, question: str, snippets: list) -> str:
        """Generates an answer using an LLM."""
        prompt = f"Context: Use the following paragraphs:\n{snippets}\n Answer the following question: {question}\n with a concise answer, if you don't know the answer just say i don't know"
        answer = self.model.invoke(prompt)

        return answer.content