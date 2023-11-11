from PyPDF2 import PdfReader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
import os


def main_chain(query):
    os.environ["OPENAI_API_KEY"] = "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"


    pdfreader = PdfReader("hero-homes-mohali-brochure1.pdf")


    from typing_extensions import Concatenate
    # read text from pdf
    raw_text = ''
    for i, page in enumerate(pdfreader.pages):
        content = page.extract_text()
        if content:
            raw_text += content



    # We need to split the text using Character Text Split such that it sshould not increse token size
    text_splitter = CharacterTextSplitter(
        separator = "\n",
        chunk_size = 800,
        chunk_overlap  = 200,
        length_function = len,
    )
    texts = text_splitter.split_text(raw_text)

    # Download embeddings from OpenAI
    embeddings = OpenAIEmbeddings()

    document_search = FAISS.from_texts(texts, embeddings)

    from pydantic import BaseModel, BaseSettings

    import re
    re.compile('<title>(.*)</title>')

    class MySettings(BaseSettings):
        my_regex: re.Pattern

        class Config:
            arbitrary_types_allowed = True





    from langchain.chains.question_answering import load_qa_chain
    from langchain.llms import OpenAI


    chain = load_qa_chain(OpenAI(), chain_type="stuff")
    query = query
    docs = document_search.similarity_search(query)
    output = chain.run(input_documents=docs, question=query)

    return output