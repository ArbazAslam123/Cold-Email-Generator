# 📧 AI Cold Email Generator

An AI-powered Cold Email Generator that extracts job details from a job posting URL, matches them with your portfolio using semantic search, and generates a personalized cold email tailored to the job requirements.

---

## 🚀 Features

* Extracts job information directly from a job posting URL.
* Cleans and processes webpage content automatically.
* Uses an LLM to identify:

  * Job Role
  * Required Experience
  * Required Skills
  * Job Description
* Performs semantic search on your portfolio using ChromaDB.
* Retrieves the most relevant portfolio projects.
* Generates a personalized cold email highlighting relevant experience and projects.
* Simple and interactive Streamlit web interface.

---

## 🛠️ Tech Stack

### AI & LLM

* LangChain
* Groq API
* GPT-OSS-120B

### Vector Database

* ChromaDB

### Frontend

* Streamlit

### Data Processing

* Pandas
* BeautifulSoup (via WebBaseLoader)

### Python Libraries

* langchain
* langchain-community
* langchain-groq
* chromadb
* pandas
* python-dotenv
* streamlit

---

## 📂 Project Structure

```text
Cold Email Generator/
│
├── App/
│   ├── main.py              # Streamlit application
│   ├── chain.py             # LLM prompts and email generation
│   ├── portfolio.py         # Portfolio vector database operations
│   ├── utils.py             # Text cleaning utilities
│   ├── resource/
│   │   └── my_portfolio.csv # Portfolio dataset
│   └── .env                # API Key
│
├── vectorstore/             # ChromaDB persistent database
├── requirements.txt
└── README.md
```

---

## ⚙️ How It Works

1. User enters a job posting URL.
2. The application scrapes the webpage content.
3. The raw HTML is cleaned and processed.
4. The LLM extracts:

   * Role
   * Experience
   * Skills
   * Description
5. The extracted skills are converted into embeddings.
6. ChromaDB searches the portfolio for the most relevant projects.
7. The selected portfolio links and job details are passed to the LLM.
8. The LLM generates a personalized cold email.
9. The generated email is displayed in the Streamlit interface.

---

## 📄 Portfolio CSV Format

The portfolio dataset should contain the following columns:

| Techstack                      | Links                                |
| ------------------------------ | ------------------------------------ |
| Python, LangChain, ChromaDB    | https://github.com/username/project1 |
| Machine Learning, Scikit-learn | https://github.com/username/project2 |

Example:

```csv
Techstack,Links
Python, LangChain, ChromaDB,https://github.com/yourusername/project1
Machine Learning, TensorFlow,https://github.com/yourusername/project2
```

---

## 🔑 Environment Variables

Create a `.env` file inside the project directory.

```env
GROQ_API_KEY=your_groq_api_key
```

---

## 📦 Installation

Clone the repository:

```bash
git clone <repository-url>
cd Cold-Email-Generator
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

### Windows

```bash
venv\Scripts\activate
```

### Linux/macOS

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

Start the Streamlit application:

```bash
streamlit run App/main.py
```

Open the local URL displayed in your terminal (typically `http://localhost:8501`).

---

## 🧠 Workflow

```text
Job URL
    │
    ▼
WebBaseLoader
    │
    ▼
Clean Text
    │
    ▼
LLM Job Extraction
    │
    ▼
Extract Skills
    │
    ▼
ChromaDB Semantic Search
    │
    ▼
Retrieve Portfolio Links
    │
    ▼
LLM Email Generation
    │
    ▼
Generated Cold Email
```

---

## 📌 Example Input

```
https://jobs.nike.com/job/R-33460
```

---

## 📌 Example Output

* Extracted Job Details
* Relevant Portfolio Projects
* Personalized AI-generated Cold Email

---

## 🔮 Future Improvements

* Support multiple LLM providers (OpenAI, Gemini, Claude, etc.).
* Generate downloadable PDF and DOCX versions of the email.
* Add email templates for different industries.
* Enable one-click email sending via SMTP or Gmail API.
* Improve extraction for JavaScript-rendered job pages.
* Cache embeddings to improve performance.
* Allow multiple portfolio datasets.

---

## 👨‍💻 Author

**Arbaz Aslam**

AI Engineer | Data Scientist

Specializing in:

* Generative AI
* AI Automation
* Agentic AI
* LangChain
* LLM Applications
* Retrieval-Augmented Generation (RAG)
* Workflow Automation

# 📧 AI Cold Email Generator

An AI-powered Cold Email Generator that extracts job details from a job posting URL, matches them with your portfolio using semantic search, and generates a personalized cold email tailored to the job requirements.

---

## 🚀 Features

* Extracts job information directly from a job posting URL.
* Cleans and processes webpage content automatically.
* Uses an LLM to identify:

  * Job Role
  * Required Experience
  * Required Skills
  * Job Description
* Performs semantic search on your portfolio using ChromaDB.
* Retrieves the most relevant portfolio projects.
* Generates a personalized cold email highlighting relevant experience and projects.
* Simple and interactive Streamlit web interface.

---

## 🛠️ Tech Stack

### AI & LLM

* LangChain
* Groq API
* GPT-OSS-120B

### Vector Database

* ChromaDB

### Frontend

* Streamlit

### Data Processing

* Pandas
* BeautifulSoup (via WebBaseLoader)

### Python Libraries

* langchain
* langchain-community
* langchain-groq
* chromadb
* pandas
* python-dotenv
* streamlit

---

## 📂 Project Structure

```text
Cold Email Generator/
│
├── App/
│   ├── main.py              # Streamlit application
│   ├── chain.py             # LLM prompts and email generation
│   ├── portfolio.py         # Portfolio vector database operations
│   ├── utils.py             # Text cleaning utilities
│   ├── resource/
│   │   └── my_portfolio.csv # Portfolio dataset
│   └── .env                # API Key
│
├── vectorstore/             # ChromaDB persistent database
├── requirements.txt
└── README.md
```

---

## ⚙️ How It Works

1. User enters a job posting URL.
2. The application scrapes the webpage content.
3. The raw HTML is cleaned and processed.
4. The LLM extracts:

   * Role
   * Experience
   * Skills
   * Description
5. The extracted skills are converted into embeddings.
6. ChromaDB searches the portfolio for the most relevant projects.
7. The selected portfolio links and job details are passed to the LLM.
8. The LLM generates a personalized cold email.
9. The generated email is displayed in the Streamlit interface.

---

## 📄 Portfolio CSV Format

The portfolio dataset should contain the following columns:

| Techstack                      | Links                                |
| ------------------------------ | ------------------------------------ |
| Python, LangChain, ChromaDB    | https://github.com/username/project1 |
| Machine Learning, Scikit-learn | https://github.com/username/project2 |

Example:

```csv
Techstack,Links
Python, LangChain, ChromaDB,https://github.com/yourusername/project1
Machine Learning, TensorFlow,https://github.com/yourusername/project2
```

---

## 🔑 Environment Variables

Create a `.env` file inside the project directory.

```env
GROQ_API_KEY=your_groq_api_key
```

---

## 📦 Installation

Clone the repository:

```bash
git clone <repository-url>
cd Cold-Email-Generator
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

### Windows

```bash
venv\Scripts\activate
```

### Linux/macOS

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

Start the Streamlit application:

```bash
streamlit run App/main.py
```

Open the local URL displayed in your terminal (typically `http://localhost:8501`).

---

## 🧠 Workflow

```text
Job URL
    │
    ▼
WebBaseLoader
    │
    ▼
Clean Text
    │
    ▼
LLM Job Extraction
    │
    ▼
Extract Skills
    │
    ▼
ChromaDB Semantic Search
    │
    ▼
Retrieve Portfolio Links
    │
    ▼
LLM Email Generation
    │
    ▼
Generated Cold Email
```

---

## 📌 Example Input

```
https://jobs.nike.com/job/R-33460
```

---

## 📌 Example Output

* Extracted Job Details
* Relevant Portfolio Projects
* Personalized AI-generated Cold Email

---

## 🔮 Future Improvements

* Support multiple LLM providers (OpenAI, Gemini, Claude, etc.).
* Generate downloadable PDF and DOCX versions of the email.
* Add email templates for different industries.
* Enable one-click email sending via SMTP or Gmail API.
* Improve extraction for JavaScript-rendered job pages.
* Cache embeddings to improve performance.
* Allow multiple portfolio datasets.

---

## 👨‍💻 Author

**Arbaz Aslam**

AI Engineer | Data Scientist

Specializing in:

* Generative AI
* AI Automation
* Agentic AI
* LangChain
* LLM Applications
* Retrieval-Augmented Generation (RAG)
* Workflow Automation
