# Movie Recommendation System

A Django-based **Movie Recommendation System** that suggests movies based on user preferences.  
This project is containerized with **Docker** for easy setup and deployment.  

---

##  Project Overview
The **Movie Recommendation System** uses **content-based filtering** to suggest movies that are similar to a selected movie.  
It matches movie similarity based on metadata like genres, keywords, cast, and crew.  

The backend is built using **Django**, and the frontend uses **HTML, CSS, and JavaScript**.  
The system can run locally or inside a **Docker container** for easy deployment.

---

##  Features
-  **Search for movies** and get similar recommendations.
-  **Content-based recommendation algorithm** using movie metadata.
-  **User-friendly web interface** with search and display functionality.
-  **Fully containerized** with Docker & Docker Compose.
-  **SQLite database** (can be swapped for PostgreSQL/MySQL).
-  Fast and lightweight — runs locally or in a container.

---

##  Tech Stack
### **Backend**
- Python 3.x
- Django 4.x
- SQLite Database

### **Frontend**
- HTML5
- CSS3
- JavaScript

### **Deployment / Containerization**
- Docker
- Docker Compose

---

##  How It Works
1. **User selects a movie** from the search bar.
2. The system fetches movie metadata from the database.
3. **Cosine similarity** is calculated between the selected movie and all other movies.
4. The top N most similar movies are returned and displayed.
5. The process works instantly with preprocessed metadata for efficiency.

---

---

## Installation & Running

### Clone the Repository**
```bash
git clone https://github.com/akhila-sinimadhula/MOVIE-RECOMMENDED-SYSTEM.git
cd MOVIE-RECOMMENDED-SYSTEM/core

docker-compose up --build

http://localhost:8000

## run without dpcker

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

http://127.0.0.1:8000


