# Week 2 — APIs & LLM Fundamentals 🤖

## 🎯 Learning Objectives

Understand how APIs work, process JSON data, explore Large Language Models (LLMs), and make the first API call to a language model using Python.

**Duration:** 5 Days  
**Study Time:** 3 Hours per Day  
**Total:** 15 Hours

## 📅 Daily Learning Plan

### Day 1 — HTTP & REST APIs
**Topics:**
- What is an API?
- Client vs. Server
- HTTP Requests and Responses
- GET and POST
- HTTP Status Codes
- Headers
- Query Parameters

**Learning Resources:**
- Corey Schafer — Python Requests Tutorial
- Requests Quickstart Documentation
- MDN — HTTP Methods

**Practice:**
- Install the requests library.
- Send a GET request.
- Print the response status code.
- Extract data from a JSON response.
- Understand status codes 200, 400, 404, and 500.
- Try a POST request.

**Daily Challenge:** Use JSONPlaceholder to retrieve Users and Posts data.

### Day 2 — JSON, APIs & Error Handling
**Topics:**
- JSON Structure
- Nested JSON
- Parsing and Serialization
- API Error Handling
- Timeouts
- Environment Variables

**Learning Resources:**
- Python JSON Documentation
- Requests — Errors and Exceptions

**Practice:**
- Receive JSON data from an API.
- Extract values from nested dictionaries.
- Convert JSON into Python dictionaries.
- Save API responses in a file.
- Add try/except to API requests.
- Configure request timeouts.
- Test an invalid API URL.

**Daily Challenge:** Build a program that retrieves user data from an API and saves it in JSON format.

### Day 3 — What Are LLMs & How Do They Work?
**Topics:**
- Generative AI
- Large Language Models (LLMs)
- Transformers — Basic Understanding
- Tokens and Tokenization
- Context Window
- Input and Output Tokens
- Temperature
- Hallucinations

**Learning Resources:**
- IBM Technology — How Large Language Models Work
- Hugging Face LLM Course — Chapter 1
- OpenAI Tokenizer

**Practice:**
- Explain the difference between AI, ML, Deep Learning, and LLMs.
- Try different sentences using a tokenizer.
- Compare the number of words with the number of tokens.
- Write an example explaining the Context Window.
- Identify three possible causes of hallucinations.

**Important:** The goal is to understand how LLMs work conceptually. Implementing a Transformer from scratch or studying its mathematics is not required at this stage.

### Day 4 — First LLM API Call
**Learning Resource:**
- DeepLearning.AI — ChatGPT Prompt Engineering for Developers
- OpenAI API Quickstart
- OpenAI Python Library Documentation

**Topics:**
- API Keys
- Python SDK
- Client Initialization
- Sending Input
- Receiving Output
- Error Handling
- Environment Variables

**Practice:**
- Create an API key from your chosen model provider.
- Install the required SDK.
- Store the API key in an environment variable.
- Write your first Python script that calls an LLM.
- Send a simple question.
- Print the model's response.
- Handle connection failures.

**Security Reminder:** Never hardcode API keys in your source code or upload them to GitHub. Use environment variables and add sensitive environment files to `.gitignore`.

### Day 5 — Mini Project: AI Text Summarizer
**Project Goal:**

Build a Python application that receives text from the user and uses an LLM to generate a summary.

**Requirements:**
- Accept text input from the user.
- Validate that the input is not empty.
- Send the text to the LLM.
- Request a clear and concise summary.
- Display the generated summary.
- Save the summary in a TXT or JSON file.
- Handle errors.

**Additional Improvements:**
Implement three summarization modes:
- Short Summary
- Detailed Summary
- Bullet Points

## 🏆 Weekly Outcome

By the end of this week, I should be able to:
- Understand REST APIs and HTTP methods.
- Send GET and POST requests using Python.
- Process JSON responses.
- Handle API errors and timeouts.
- Understand LLMs, tokens, and context windows.
- Make an LLM API call using Python.
- Build a basic AI-powered application.

## ✅ Project Checklist

- [ ] Python Functions
- [ ] API Request
- [ ] JSON Handling
- [ ] Environment Variables
- [ ] LLM Integration
- [ ] Error Handling
- [ ] Save Summary to TXT or JSON
- [ ] Project README
- [ ] Push Project to GitHub

## 🚀 Milestone 1 — Python + LLM Basics

At the end of the first two weeks, the expected GitHub projects are:

1. Text Processing Tool
2. API Data Fetcher
3. AI Text Summarizer

The goal is to move from Python fundamentals to building a real application powered by an LLM.

---

**Key Principle:** Don't just learn how to call an API. Understand the request, the response, the data, and how the LLM fits into the application.
