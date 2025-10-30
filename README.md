Book Recommender Web App
Overview

This is a full-stack web application that recommends books based on genres.
The backend is built with FastAPI (Python) and the frontend with React.js.
It demonstrates how to connect a Python API to a modern frontend.

Features

Genre-based book recommendation

RESTful API using FastAPI

Responsive frontend with React and CSS

Simple and clean UI design

Technologies Used

Frontend: React.js, Axios, CSS

Backend: FastAPI, Python

Server: Uvicorn

Setup Instructions
Backend (FastAPI)
cd book-recommender
python3 -m venv venv
source venv/bin/activate
pip install fastapi uvicorn
uvicorn main:app --reload

Frontend (React)
cd book-recommender-ui
npm install
npm start

API Endpoints
Method	Endpoint	Description
GET	/books	Fetch all books
GET	/recommend/{genre}	Get books by genre
Future Improvements

Integrate real AI-based recommendations

Add book cover images

Include login and user preferences