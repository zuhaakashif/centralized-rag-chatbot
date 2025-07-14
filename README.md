# 🔎🧠 Retrieval-Augmented Generation (RAG) System with TF-IDF + LLM API

This project is a centralized Retrieval-Augmented Generation (RAG) system built using **Streamlit**, **TF-IDF-based document retrieval**, and **online LLM APIs** (via OpenRouter). It allows multiple users to interact with a chatbot that gives **accurate, grounded responses** by first retrieving relevant context from a knowledge base before generating answers.

---

## 🚀 Features

- 🔍 **TF-IDF Vector Search**: Finds the most relevant documents from your knowledge base.
- 🧠 **Online LLM API Integration**: Uses a Language Model to generate responses based on the retrieved data.
- 🌐 **Streamlit UI**: Clean and interactive interface for chatting with the RAG system.
- 🧵 **Centralized Knowledge Base**: One source of truth for multiple users.
- 💡 Ideal for educational tools, customer support bots, or research assistants.

---

## 📷 Preview

![UI Screenshot](Screenshot%202025-07-14%20201649.png) 

---
![UI Screenshot](Screenshot%202025-07-14%20201934.png)

---
![UI Screenshot](Screenshot%202025-07-14%20201954.png)

---

## 🛠️ Tech Stack

- Python 🐍  
- Streamlit 🌐  
- Scikit-learn (TF-IDF) 📊  
- OpenRouter API / Other LLM APIs 🤖  
- NumPy, pandas  

---

## 📂 Project Structure

```

📁 rag-tfidf-app/
├── app.py               # Streamlit app code
├── retriever.py         # TF-IDF-based document retriever
├── llm\_api.py           # Handles API calls to the LLM
├── data/
│   └── knowledge\_base.txt  # Text documents used for retrieval
├── requirements.txt     # Dependencies
└── README.md            # Project overview

````

---

## 🧠 How It Works (Non-Technical)

Imagine you're asking a very smart person a question.  
But instead of guessing, they first search a set of documents to find the most relevant information.  
Then, they use that info to give you a smart and accurate answer.

That’s exactly what this system does:
1. **Retrieves** relevant documents using TF-IDF  
2. **Generates** an answer using a Language Model API

---

## 📦 Installation

1. **Clone the repo:**

```bash
git clone https://github.com/your-username/rag-tfidf-app.git
cd rag-tfidf-app
````

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Set up your API key:**
   Edit `llm_api.py` and add your API key from OpenRouter or another provider:

```python
headers = {
    "Authorization": "Bearer YOUR_API_KEY",
    "Content-Type": "application/json"
}
```

4. **Run the Streamlit app:**

```bash
streamlit run app.py
```

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

```

---

Let me know if you'd like to:
- Embed an animated preview (GIF)
- Add instructions to upload PDFs instead of `.txt` files
- Dockerize the app  
- Include tips for deploying to platforms like Hugging Face Spaces or Streamlit Cloud

Just say the word!
```
