from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

class Embeddings:
    def __init__(self):
        self.data_path = "data/Attention.pdf"
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.embedding_function = OpenAIEmbeddings(model="text-embedding-3-large", api_key=self.api_key)

    def load_data(self):
        loader = PyPDFLoader(self.data_path)
        docs = loader.load()
        text_splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n"],
        chunk_size=1000,
        chunk_overlap=50
        )

        paragraphs = text_splitter.split_documents(docs)
        return paragraphs

    def get_embeddings(self, paragraphs):
        vector_store = Chroma(embedding_function=self.embedding_function)
        vector_store.add_documents(paragraphs)
        return vector_store
    
    def get_relevant_snippets(self, query, n_results=3):
        paragraphs = self.load_data()
        retriever = self.get_embeddings(paragraphs)
        relevant_snippets = retriever.similarity_search(query, k=n_results)
        content = [snippet.page_content for snippet in relevant_snippets]
        return content