## Code Challenge Generator

Streamlit web application for generating technical coding challenges using language models via LangChain. Configure programming language, seniority level, and topic to get a problem statement, test cases, and a reference solution.

### Features

- **Custom challenge generation**: set language, seniority level, and challenge topic.
- **Complete challenge structure**: title, description, test cases (visible and hidden), and suggested solution.
- **Interactive Streamlit UI**: sidebar form for configuration and tabs for description, tests, and solution.

### Main technologies

- **Python 3.10+**
- **Streamlit** for the web interface.
- **LangChain + OpenAI (ChatOpenAI)** for challenge generation.
- **Pydantic** for typing and validation of challenge structure.
- **python-dotenv** for loading environment variables.

---

## Installation and running

### Prerequisites

- **Python 3.10 or higher** installed.
- A valid API key for the provider configured in `ChatOpenAI` (by default, OpenAI-compatible via `langchain_openai`).

### Installation steps

1. **Clone the repository**

```bash
git clone <repository-url>
cd code-challenge-generator
```

2. **Create and activate a virtual environment (optional, recommended)**

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate   # Windows (PowerShell)
```

3. **Install dependencies**

If a requirements file exists (e.g. `requirements.txt`):

```bash
pip install -r requirements.txt
```

Otherwise, install the main packages manually:

```bash
pip install streamlit langchain-openai python-dotenv pydantic
```

4. **Configure environment variables**

Create a `.env` file in the project root and set the keys required by `ChatOpenAI`, for example:

```bash
OPENAI_API_KEY=your_token_here
OPENAI_BASE_URL=https://api.openai.com/v1  # adjust if using another compatible endpoint
```

Exact variable names may vary depending on the provider configured in your setup. Ensure they are compatible with `langchain_openai.ChatOpenAI`.

5. **Run the application**

From the project root:

```bash
streamlit run src/app.py
```

The app will be available at something like `http://localhost:8501`.

---

## How to use

1. Open the application in your browser.
2. In the sidebar:
   - **Programming language**: select the target language (Python, JavaScript, TypeScript, Go, Java, SQL, C++).
   - **Seniority level**: choose the level (Junior, Mid-Level, Senior, Staff/Principal).
   - **Challenge topic**: enter the challenge topic (e.g. REST API, Dynamic programming, Sorting algorithms).
3. Click **Generate challenge**.
4. After generation, use the tabs:
   - **Description**: full problem statement.
   - **Test cases**: list of test cases with input, expected output, and whether each is hidden.
   - **Suggested solution**: reference implementation in the selected language.

If generation fails (network issues, invalid keys, etc.), an error message will be shown in the UI.

---

## Project structure

Main files and directories:

- `src/app.py`: Streamlit app, UI definition, interaction flow, and challenge display.
- `src/core/generator.py`: LangChain and `ChatOpenAI` integration, prompt definition, and `generate_challenge` function.
- `src/core/models.py`: Pydantic models for the challenge (`Challenge`) and test cases (`TestCase`).

---

## Architecture decisions

- **Separation between UI and domain layer**
  - The interface (`src/app.py`) is responsible only for orchestrating user interaction, collecting parameters, and rendering results.
  - Challenge generation logic and data contracts live in `src/core`, keeping Streamlit decoupled from business rules.

- **Typed models with Pydantic**
  - The `Challenge` and `TestCase` models explicitly define the structure of generated data.
  - This simplifies validation, schema evolution, and integration with tools that support `BaseModel`.

- **Structured generation with LangChain**
  - The `generate_challenge` function uses `ChatPromptTemplate` and `with_structured_output(Challenge)` so the model output matches the expected format.
  - This reduces manual text post-processing and lowers the risk of inconsistency between front-end and back-end.

- **External configuration via `.env`**
  - Using `python-dotenv` and environment variables allows changing API keys and model endpoints without modifying source code.
  - Keeps credentials out of the repository, in line with security best practices.

- **Language mapping for code highlighting**
  - The `CODE_LANGUAGE_MAP` dictionary in `app.py` maps the chosen language name to the identifier used by `st.code`.
  - This enables correct syntax highlighting for the solution while keeping the UI layer simple and extensible (add new entries to the map as needed).

---

## Possible future improvements

- **Support for multiple LLM providers** with configuration via UI or environment variables.
- **History of generated challenges** with persistence in a database or local file.
- **Export challenges** to formats such as Markdown or PDF.
- **Basic authentication** for internal use by recruiting or engineering teams.
