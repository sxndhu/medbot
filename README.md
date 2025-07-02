# Medbot - A Medical Screening Assistant

Medbot is an intelligent medical screening assistant that integrates advanced AI technologies, machine learning, and web development frameworks to aid healthcare professionals — especially nurses — in streamlining patient screening and administrative tasks.

## 🚀 Project Overview

The goal of this project is to combine the power of OpenAI’s GPT model with our own disease prediction engine and the robustness of the Django web framework to build an all-in-one assistant for medical screening.

Medbot assists in:
- Disease prediction using machine learning models
- AI-powered chat interaction for patient screening
- Handling administrative workflows in a seamless web application

## ⚙️ Tech Stack

- **Backend**: Django 4.2 (Python 3.9+)
- **Frontend**: Bootstrap, HTML/CSS, JavaScript
- **Database**: PostgreSQL
- **AI/ML**: 
  - OpenAI GPT integration
  - Scikit-learn: SVC, RandomForestClassifier, GaussianNB
  - NumPy, Pandas, SciPy

## 🧠 Features

- 🔍 AI Chatbot powered by GPT to assist during patient screenings
- 📊 Machine learning-based disease prediction
- 🖥️ Admin panel and user management via Django
- 📝 Support for storing patient records and screening outputs
- 💬 Real-time interface for nurse–patient interaction

## 🔐 Security

- Sensitive files such as API keys (`chatapp/open_ai_key.py`) and environment variables (`.env`) are excluded via `.gitignore`.
- Ensure not to commit any secrets to the public repo.
