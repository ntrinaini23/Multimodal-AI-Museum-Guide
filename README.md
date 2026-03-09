# Multimodal AI Museum Guide

The Multimodal AI Museum Guide is a web-based application that provides an interactive way for users to explore museum artifacts and learn about their historical significance using artificial intelligence. The system allows users to view artifact images, read descriptions, and interact with an AI-powered chatbot that answers questions about each artifact.

This project combines web development technologies with an AI model to create a digital museum guide that enhances the learning experience for visitors.

---

## Features

- User Authentication (Login and Signup)
- Artifact Gallery Dashboard
- Artifact Detail Pages with Images and Descriptions
- AI-powered Chatbot for Artifact Questions
- Dark Themed User Interface
- Interactive Chat on Artifact Pages

---

## Technologies Used

### Frontend
- HTML
- CSS
- JavaScript

### Backend
- Python
- Flask

### AI Integration
- Groq API
- Llama AI Model

### Database
- SQLite

---

## Project Structure

```
multimodal-museum-guide
│
├── app.py
├── users.db
├── requirements.txt
│
├── data
│   └── artifacts.json
│
├── models
│   └── ai_chatbot.py
│
├── static
│   ├── css
│   │   └── styles.css
│   │
│   ├── images
│   │
│   └── js
│
└── templates
    ├── base.html
    ├── login.html
    ├── signup.html
    ├── dashboard.html
    └── artifact.html
```

---

## How It Works

1. Users log in or create an account.
2. After login, users are redirected to the artifact dashboard.
3. The dashboard displays a collection of museum artifacts.
4. Users can click on an artifact to view its image and description.
5. A chatbot is available on the artifact page where users can ask questions about the artifact.
6. The AI generates responses using the Groq API.

---

## Installation

Clone the repository:

```
git clone https://github.com/yourusername/multimodal-museum-guide.git
```

Navigate to the project folder:

```
cd multimodal-museum-guide
```

Create a virtual environment:

```
python -m venv venv
```

Activate the virtual environment:

Linux / Mac:
```
source venv/bin/activate
```

Windows:
```
venv\Scripts\activate
```

Install dependencies:

```
pip install -r requirements.txt
```

Run the application:

```
python app.py
```

Open the browser and go to:

```
http://127.0.0.1:5000
```

---

## Future Enhancements

- Voice-based AI guide
- Multi-language support
- Artifact search functionality
- 3D artifact visualization
- Admin dashboard for artifact management

---

## Conclusion

The Multimodal AI Museum Guide demonstrates how artificial intelligence can enhance museum experiences by providing interactive explanations and allowing visitors to learn more about artifacts through AI-powered conversations.
