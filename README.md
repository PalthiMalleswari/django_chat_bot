# Django Chatbot Application  

A chatbot application built using **Django**, **Python**, **PostgreSQL**, **HTML**, **CSS**, and **Gemini APIs**. This application provides personalized chat experiences for users with authentication and a unique homepage for each user.  

---

## Features  

### Core Functionality:  
- **Chatbot Interaction**:  
  - Users can ask queries, and the chatbot provides accurate responses using Gemini APIs.  

### User Management:  
- **User Authentication**:  
  - Register new users with a secure registration system.  
  - Login functionality for returning users.  
- **Personalized Home Page**:  
  - Each user gets a unique homepage to manage chats and queries.  

---

## Tech Stack  
- **Backend**: Django, Python  
- **Database**: PostgreSQL  
- **Frontend**: HTML, CSS  
- **APIs**: Gemini APIs  

---
## Demo
[Video](https://www.youtube.com/watch?v=nx5hr7AaBiI)
---
## Prerequisites  
- Python 3.8+  
- pip (Python package installer)  
- PostgreSQL  
- Django 4.0+  

---

## Setup Instructions  

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/PalthiMalleswari/django-chat_bot.git
   cd django-chatbot

2. **Create a Virtual Environment**

    ```bash
    python -m venv chatbot_env  
    source chatbot_env/bin/activate  # On Windows: chatbot_env\Scripts\activate

3. **Install Dependencies**
      ```bash
      pip install -r requirements.txt

4. **Configure the Database**

    Update the DATABASES setting in settings.py to match your PostgreSQL credentials.
    Apply Migrations
   
5. **Apply Migrations**
    ```bash
    python manage.py makemigrations  
    python manage.py migrate  
    Run the Development Server
6. **Run the Development Server**

    ```bash
    python manage.py runserver
7. **Access the Application**
  Open your browser and navigate to: http://127.0.0.1:8000/
