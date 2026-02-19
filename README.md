# 📄 AI PDF Summarizer

An AI-powered PDF Summarization web application built using **Streamlit, LangChain, and Google Gemini (LLM)**.

This project enables users to upload any PDF document and receive a **structured, detailed summary** generated using advanced large language model techniques.

---

## 🚀 Key Features

- 📂 Upload and analyze any PDF document
- 🧠 Intelligent long-document summarization
- 📑 Structured and comprehensive output
- ⚡ Efficient handling of large documents using Map-Reduce strategy
- 🔐 Secure API key management using environment variables
- 🎯 Clean and responsive Streamlit interface

---

## 🧠 Core Concept

Large PDFs cannot be processed in a single pass due to token limits.

This application implements a **Map-Reduce Summarization Architecture**:

1. Extract text from PDF
2. Split text into manageable chunks
3. Generate partial summaries for each chunk (Map Step)
4. Combine all partial summaries into one detailed final summary (Reduce Step)

This ensures:
- Scalability
- Better summary quality
- Efficient token usage
- Extensibility for future features

---

## 🛠 Technology Stack

- **Python**
- **Streamlit** (Frontend Interface)
- **LangChain** (LLM Orchestration)
- **Google Gemini** (Large Language Model)
- **PyPDF** (Text Extraction)
- **python-dotenv** (Secure API management)

---

## 🏗 Project Structure
pdf-summarizer/
│
├── main.py # Streamlit application entry point
├── utils.py # Core summarization logic
├── requirements.txt # Project dependencies
├── README.md # Project documentation
├── .gitignore # Ignored files
└── .env # Environment variables (not tracked)


---

## 🔐 Security Design

- No API keys are hardcoded
- Environment variables handled via `.env`
- `.gitignore` prevents sensitive data from being uploaded

---

## 📈 Future Enhancements

- 💬 Chat with PDF functionality
- 📌 Key points extraction mode
- 📝 Executive summary generation
- 📊 Downloadable summaries (PDF / DOCX)
- 🌐 Cloud deployment
- 🔐 Authentication & user sessions

---

## 🧪 Use Cases

- Academic paper summarization
- Business report analysis
- Legal document overview
- Technical documentation review
- Research content condensation

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 👨‍💻 Author

AI project built using modern LLM architecture principles with LangChain and Google Gemini.

---

⭐ If you found this project useful, consider giving it a star on GitHub!

