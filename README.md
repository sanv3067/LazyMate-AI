# LazyMate AI 🦥

**Turn rough study notes into a useful study pack—with a local open-weight AI model.**

LazyMate is a small, beginner-friendly study workflow assistant. Paste or upload lecture notes and ask it to create a study pack, summarize the content, generate revision questions, or turn it into an action checklist.

## Why this fits “Slow and Steady”

The goal is simple: spend less time formatting notes and more time learning. LazyMate automates the repetitive first pass—organizing information into a format that is easier to revise.

## Features

- Study pack: overview, key points, definitions, revision questions, and a 10-minute revision plan.
- Quick summary with key takeaways.
- Revision questions with an answer key.
- Action checklist for what to study first.
- Output in simple English, Tamil, or English + Tamil.
- Download generated output as Markdown.
- Local inference through Ollama; no hosted AI API is used by the app.
- Accepts `.txt` and `.md` notes.

## How the AI works

LazyMate sends the notes and task instructions to the Ollama API running at `http://localhost:11434`. The default model is `gemma3:1b`, an open-weight Gemma model available through Ollama. The model generates the answer on the local computer.

**Privacy note:** The app itself sends prompts only to the local Ollama endpoint. Internet access is required to install Python packages and download the model initially. Once installed, generation can run without internet, assuming Ollama and the model are available locally. Do not paste sensitive information into any AI tool unless you understand the risks of your setup.

## Requirements

- Python 3.10 or newer
- Ollama
- About 1 GB or more of free disk space for the model, plus room for Python packages and app files
- 8 GB RAM is a reasonable starting point for the small `gemma3:1b` model, but speed depends on your CPU/GPU and other apps running

## Run locally

### 1. Install Ollama

Install it from [ollama.com/download](https://ollama.com/download), then open Ollama.

### 2. Download the model (one-time setup)

Open a terminal / Command Prompt and run:

```bash
ollama run gemma3:1b
```

The first download needs internet and may take time on limited data. Wait for the model to download. At the prompt, type `hi` to confirm it responds, then type `/bye` to exit.

### 3. Set up the Python app

In the project folder:

```bash
python -m venv .venv
```

Activate the environment:

**Windows PowerShell**
```powershell
.\.venv\Scripts\Activate.ps1
```

**Windows Command Prompt**
```bat
.venv\Scripts\activate.bat
```

**macOS / Linux**
```bash
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

### 4. Start LazyMate

```bash
streamlit run app.py
```

Streamlit will show a local URL, usually `http://localhost:8501`. Open it in your browser. Keep Ollama running while using the app.

If the model is already downloaded, LazyMate's AI generation does not need an internet connection.

## Try it

Open `sample_notes.md`, copy the text into LazyMate, choose **Create a study pack**, and press **Generate**.

## Troubleshooting

- **Cannot connect to Ollama:** Open the Ollama desktop app, or start the Ollama service. Then try `ollama run gemma3:1b`.
- **Model not found:** Run `ollama run gemma3:1b` and wait for setup to finish.
- **Slow response:** Close other apps, shorten the notes, and try again.
- **Not enough memory:** Use a smaller model supported by your Ollama installation or close memory-heavy apps.
- **Tamil output varies:** Ask for shorter answers or regenerate. Always verify facts before exams.

## Tests

The lightweight static checks can be run with:

```bash
python -m pip install pytest
python -m pytest
```

These tests check app configuration and workflow labels; they do not replace a full manual test with Ollama.

## Demo checklist

Before recording or taking screenshots:

1. Start Ollama and confirm `gemma3:1b` works.
2. Run `streamlit run app.py`.
3. Load `sample_notes.md`.
4. Generate a study pack.
5. Show the Tamil or English + Tamil option.
6. Download the Markdown output.
7. Record a short screen capture showing the full workflow.

## Project limitations

- Only `.txt` and `.md` uploads are supported in this first version.
- Output quality depends on the model and source notes; it can make mistakes.
- This is a prototype, not a replacement for textbooks or teacher guidance.

## Roadmap

- [ ] Add PDF extraction
- [ ] Add saved local study-pack history
- [ ] Add source-grounded answer checks
- [ ] Add optional export to a printable PDF
- [ ] Add tests for prompt construction and error handling

## License

MIT. See [`LICENSE`](LICENSE).

## Challenge submission

This project was created for the DEV Community Hacktoberfest Open-Source AI Challenge: Week 3. The submission should include a demo and a DEV post tagged `#devchallenge` and `#hf26challenge`. Do not claim a hosted demo, test result, or feature unless you have personally verified it.
