# AI Ops Assistant (GenAI Intern Assignment)

This project is an AI Operations Assistant built as part of the GenAI Intern assignment.
It accepts a natural-language task, plans execution steps using an LLM, executes those
steps using real APIs, verifies results, and returns a structured end-to-end response.

---

## Architecture Overview

The system follows a **multi-agent architecture**:

1. **Planner Agent**
   - Converts user tasks into a structured JSON plan
   - Uses an LLM with constrained output
   - Includes fallback planning for reliability

2. **Executor Agent**
   - Executes each step in the plan
   - Calls real third-party APIs
   - Handles failures gracefully without crashing

3. **Verifier Agent**
   - Validates execution results
   - Ensures a complete end-to-end response

---

## Integrated APIs

- **GitHub API**
  - Searches and retrieves top repositories by stars
- **OpenWeatherMap API**
  - Fetches current weather information by city

---

## Project Structure

