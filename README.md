# 🤖 CoverBot

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![LangChain](https://img.shields.io/badge/LangChain-Latest-green.svg)
![OpenAI](https://img.shields.io/badge/OpenAI-Latest-orange.svg)
![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)

## 🎯 Overview
CoverBot is an intelligent chatbot powered by Large Language Models (LLM) and Retrieval-Augmented Generation (RAG) that helps users analyze documents and extract meaningful insights through natural conversation.

## 🔍 What's happening?
1. The user uploads a cover letter or other type of document which needs to be analyzed
2. CoverBot retrieves text data and gets ready to answer all important questions which the user is interested in document
3. Interactive conversation helps users understand their documents better

## ✨ Key Features
- 📄 Document Upload & Analysis
- 💬 Natural Language Q&A
- 🔍 Smart Context Retrieval
- 🎯 Focused Document Insights
- ⚡ Real-time Response Generation

## 🛠️ Tech Stack
- **Backend Framework:** FastAPI
- **LLM Integration:** LangChain
- **Vector Database:** Pinecone
- **Language Model:** OpenAI GPT-4
- **Frontend:** Streamlit
- **Document Processing:** PyPDF2, docx2txt

## 🚀 Installation Guide

### System Requirements
- Python 3.8+
- pip (Python package installer)
- Git
- Virtual environment (recommended)

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/coverbot.git
cd coverbot
```

### 2. Set Up Virtual Environment
```bash
# For Windows
python -m venv venv
.\venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
# Core dependencies
pip install -r requirements.txt

# Additional dependencies
pip install streamlit fastapi uvicorn langchain openai pinecone-client python-dotenv
pip install pypdf2 python-docx docx2txt
```

### 4. Environment Configuration
Create a `.env` file in the root directory:
```bash
touch .env
```

Add the following to your `.env` file:
```env
OPENAI_API_KEY=your_openai_api_key
PINECONE_API_KEY=your_pinecone_api_key
PINECONE_ENV=your_pinecone_environment
MODEL_NAME=gpt-4
STREAMLIT_SERVER_PORT=8501
```

### 5. Database Setup
```bash
# Initialize Pinecone database
python scripts/init_db.py
```

### 6. Running the Application
```bash
# Start the backend server
uvicorn app.main:app --reload --port 8000

# In a new terminal, start the frontend
streamlit run frontend/app.py
```

### 7. Verify Installation
- Backend API: http://localhost:8000/docs
- Frontend: http://localhost:8501

## 📦 Project Structure
```
coverbot/
├── app/
│   ├── main.py
│   ├── models.py
│   └── utils.py
├── frontend/
│   └── app.py
├── scripts/
│   └── init_db.py
├── tests/
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## 🔧 Troubleshooting

### Common Issues

1. **OpenAI API Error**
```bash
# Check API key
echo $OPENAI_API_KEY
# Verify API access
python -c "import openai; openai.api_key='your-key'; print(openai.Model.list())"
```

2. **Pinecone Connection Issues**
```bash
# Verify Pinecone environment
python scripts/test_pinecone.py
```

3. **Port Already in Use**
```bash
# Kill process using port 8000
lsof -i :8000
kill -9 <PID>
```

## 📊 Features in Development
- 🔘 Interactive buttons with recommended questions for faster workflow
- 📱 Mobile-Responsive UI
- 🔄 Batch Processing
- 📊 Analytics Dashboard
- 🔐 User Authentication

## 🎯 Use Cases
- 📝 Cover Letter Analysis
- 📄 Resume Screening
- 📑 Document Summarization
- ❓ FAQ Generation
- 📈 Content Analysis

## 🤝 Contributing
We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## 📧 Contact
- **Creator:** Edgar Abasov
- **Email:** edgarabasov1@gmail.com
- **LinkedIn:** www.linkedin.com/in/edgar-abasov/


