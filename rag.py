import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import requests

st.set_page_config(page_title="OpenRouter RAG", layout="centered")
st.title("🌐 Centralized RAG using OpenRouter API")

# --- Sample knowledge base ---
documents = [
    "LLMs are large models trained on internet text to predict next words.",
    "RAG improves answers by retrieving relevant documents and combining them with generation.",
    "TinyLLaMA is a small language model that can run locally without internet.",
    "Vector databases like FAISS help search for relevant text chunks.",
    "Open-source LLMs are useful for local inference without API cost."
]

# --- Retrieve relevant document using TF-IDF ---
def retrieve_context(query, docs):
    vect = TfidfVectorizer().fit_transform([query] + docs)
    similarity = cosine_similarity(vect[0:1], vect[1:])
    best_idx = similarity.argmax()
    return docs[best_idx]

# --- Query OpenRouter API ---
def query_openrouter_llm(context, question):
    prompt = f"""You are a helpful assistant. Use ONLY the context below to answer the question.
If the context is not relevant, say "I don't know."

Context: {context}
Question: {question}
Answer:"""

    headers = {
        "Authorization": f"Bearer {st.secrets['OPENROUTER_API_KEY']}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "mistralai/mistral-7b-instruct",  
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", json=data, headers=headers)
    
    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        return f"Error: {response.status_code} - {response.text}"

# --- UI ---
user = st.selectbox("Select User", ["User A", "User B", "User C"])

with st.form("query_form"):
    query = st.text_input("Ask your question:", placeholder="e.g. What is RAG?")
    submitted = st.form_submit_button("Submit")

if submitted and query:
    with st.spinner("Retrieving context and querying LLM..."):
        context = retrieve_context(query, documents)
        answer = query_openrouter_llm(context, query)

    st.markdown("---")
    st.subheader("🔍 Retrieved Context")
    st.write(context)

    st.subheader("🤖 LLM's Answer (via OpenRouter)")
    st.write(answer)

    st.markdown("---")
    st.caption(f"Response generated for {user} using OpenRouter API")




