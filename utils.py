from langchain_text_splitters import CharacterTextSplitter
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_classic.chains.summarize import load_summarize_chain
from langchain_classic.docstore.document import Document
from langchain_classic.prompts import PromptTemplate
from pypdf import PdfReader


def summarizer(pdf):
    if pdf is not None:
        pdf_reader = PdfReader(pdf)
        text = ""

        for page in pdf_reader.pages:
            text += page.extract_text() or ""

        # Split text
        text_splitter = CharacterTextSplitter(
            chunk_size=2000,
            chunk_overlap=200
        )

        docs = [
            Document(page_content=chunk)
            for chunk in text_splitter.split_text(text)
        ]

        # Initialize Gemini model
        llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            temperature=0.2
        )

        # ✅ MAP PROMPT (for each chunk)
        map_prompt = PromptTemplate(
            template="""
            Write a detailed summary of the following text chunk.
            Focus on key ideas, arguments, and important points.

            {text}
            """,
            input_variables=["text"]
        )

        # ✅ COMBINE PROMPT (final summary)
        combine_prompt = PromptTemplate(
            template="""
            You are an expert summarization assistant.

            Combine the following partial summaries into one
            comprehensive, well-structured, and detailed final summary.

            Include:
            - Main themes
            - Important arguments
            - Key findings
            - Final conclusion

            Make the summary detailed but clear and professional.

            {text}
            """,
            input_variables=["text"]
        )

        # Create summarization chain
        chain = load_summarize_chain(
            llm,
            chain_type="map_reduce",
            map_prompt=map_prompt,
            combine_prompt=combine_prompt
        )

        summary = chain.run(docs)

        return summary
