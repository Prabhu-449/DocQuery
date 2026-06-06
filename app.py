import streamlit as st
from dotenv import load_dotenv
load_dotenv()

from utils.document_loader import extract_text
from rag.text_splitter import split_text
from src.embeddings import create_vectorstore
from src.qa_chain import get_qa_chain



st.set_page_config(
    page_title="DocQuery",
    page_icon="📄",
    layout="wide"
)

with st.sidebar:

    st.title("📄 DocQuery")

    st.markdown("---")

    st.markdown("""
    ### Features

        [PDF Upload]✅
        [Semantic Search]✅
        [AI Answers]✅
        [FAISS Vector DB]✅
        [Groq LLM]✅
        [HuggingFace Embeddings]✅
    """)

    st.markdown("---")

    st.info(
        "Built using Streamlit, LangChain, FAISS, and Groq"
    )


st.markdown("""
# 📄 DocQuery

### AI-Powered RAG Document Q&A Assistant

Upload documents and ask intelligent questions using
semantic search and LLM-powered retrieval.
""")

st.markdown("---")

st.subheader("📤 Upload Document")

uploaded_files = st.file_uploader(
    "Upload PDF or DOCX files",
    type=["pdf", "docx"],
    accept_multiple_files=True
)


if uploaded_files:

    all_text = ""

    for uploaded_file in uploaded_files:

        st.success(
            f"Successfully uploaded: {uploaded_file.name}"
        )

        with st.spinner("Extracting text..."):

            extracted_text = extract_text(uploaded_file)

            all_text += extracted_text + "\n\n"

    with st.spinner("Splitting text into chunks..."):

        chunks = split_text(all_text)

    with st.spinner("Creating vector database..."):

        vector_store = create_vectorstore(chunks)

    st.success("Vector database ready")

    st.write(f"Total Chunks: {len(chunks)}")

    user_question = st.text_input(
    "Ask a question about the document"
)

if user_question:

    docs = vector_store.similarity_search(
        user_question,
        k=3
    )

    chain = get_qa_chain()

    context = "\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
You are DocuQuery, a professional AI document assistant.

Answer the user's question using ONLY the document context below.

Document Context:
{context}

User Question:
{user_question}

Final Answer:
"""

    response = chain.invoke(prompt)

    st.markdown("---")

    st.subheader("🤖 AI Answer")

    st.info(response.content)

    st.download_button(
        label="⬇️ Download Answer",
        data=response.content,
        file_name="docuquery_answer.txt",
        mime="text/plain"
    )

    st.markdown("---")

    st.subheader("📚 Source Chunks")

    for i, doc in enumerate(docs):

        with st.expander(f"Source {i+1}"):

            st.write(doc.page_content)