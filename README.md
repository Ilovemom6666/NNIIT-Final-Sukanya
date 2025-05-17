# Flashcard

This is the backend for my smart flashcard system project. The goal is to let users add flashcards with just questions and answers, and the system will automatically figure out the subject of each flashcard. Later, students can request flashcards from different subjects, and the API will return a mixed batch for effective studying.

Problem Statement:
You need to build a backend for a smart flashcard system. Users add flashcards containing a question and answer but do not specify the subject. The backend must automatically determine the subject based on the question text using keyword matching or a classification model.

Students can later request flashcards by subject, and the system should return a mixed batch of flashcards intelligently.

Tasks
Task 1:

Add Flashcard with Subject Inference
Create a POST endpoint /flashcard that accepts:

{
  "student_id": "stu001",
  "question": "What is Newton's Second Law?",
  "answer": "Force equals mass times acceleration"
}

The backend infers the subject (e.g., "Physics") based on the question and stores:
student_id
question
answer
subject
Return a confirmation message along with the inferred subject.


Task 2:

Get Flashcards by Mixed Subjects
Create a GET endpoint /get-subject that accepts query parameters:
student_id
limit (number of flashcards to return)
Return up to limit flashcards for the specified student, mixing subjects randomly.

How It Works ?
1.Adding Flashcards
I created a POST endpoint /flashcard where users send the student ID, question, and answer.

The backend automatically detects the subject using a keyword-based rule system (or a model if I choose to enhance it later).

Example request:
{
  "student_id": "stu001",
  "question": "What is Newton's Second Law?",
  "answer": "Force equals mass times acceleration"
}
Example response:
{
  "message": "Flashcard added successfully",
  "subject": "Physics"
}

2.Getting Flashcards by Subject
I also made a GET endpoint /get-subject where students can request a batch of flashcards filtered by their ID.

Query parameters:
student_id — the student requesting flashcards.
limit — how many flashcards to return.
The response returns a shuffled mix of flashcards from different subjects, up to the requested limit.

Example request:
GET /get-subject?student_id=stu001&limit=5

Example response:
[
  {
    "question": "What is Newton's Second Law?",
    "answer": "Force equals mass times acceleration",
    "subject": "Physics"
  },
  {
    "question": "What is photosynthesis?",
    "answer": "A process used by plants to convert light into energy",
    "subject": "Biology"
  }
]

Installation:
Python 3.7+ installed.
FASTAPI
Uvicorn

Notes:
Subject inference currently uses a rule-based keyword matching system.
