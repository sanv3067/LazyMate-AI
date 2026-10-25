# LazyMate AI: Let a Local Open-Weight Model Do the First Pass of Studying

I built LazyMate AI for a familiar student problem: the hardest part of revision is sometimes not learning the topic, but turning rough notes into something usable.

LazyMate takes pasted or uploaded text notes and uses a local Gemma model through Ollama to create a study pack, quick summary, revision questions, or a checklist. It can write in simple English, Tamil, or a mix of both.

## The idea: automate the boring first pass

Students often repeat the same small tasks:
- reread a long page to find the main points;
- rewrite definitions into short notes;
- invent practice questions;
- decide what to revise first.

LazyMate gives those tasks a starting point. Instead of manually formatting everything, a student can generate a draft and spend their time checking, correcting, and learning it.

## How it works

1. The student pastes notes or uploads a `.txt` / `.md` file.
2. They choose one workflow: study pack, summary, revision questions, or action checklist.
3. The app builds a task-specific prompt and sends it to the Ollama service running on the same computer.
4. The local Gemma model generates the result.
5. The student reviews it and can download the result as Markdown.

The project uses Python and Streamlit for the interface, and Ollama to run the model locally.

**Code:** [Add your GitHub repository URL here]  
**Demo:** [Add a short demo video or deployed demo URL here]

## Why open innovation matters here

For this project, local open-weight AI is not just a technical detail. It changes the practical trade-off.

**Privacy:** The app sends the notes to a local Ollama endpoint rather than a hosted AI API. That means the app does not need to upload study notes to a third-party model service. Users should still understand their own computer setup and avoid entering sensitive information unnecessarily.

**Control:** The model name can be changed in the sidebar or with the `OLLAMA_MODEL` environment variable. That makes it possible to experiment with other locally available Ollama models without rebuilding the whole interface.

**Cost:** After downloading the model, generating study packs does not require a per-request hosted AI API from this app. The trade-off is that local inference uses the computer's memory, CPU/GPU, and electricity.

**Offline use:** The initial setup needs internet to install packages and download the model. After that, generation can work offline as long as the model is installed and Ollama is running.

## What I learned

The project taught me to separate the user interface from model inference, handle connection and timeout errors, and be honest about limitations. A local model can be slower than a hosted service, and it can still make mistakes. LazyMate therefore treats its output as a draft for revision, not as an unquestionable answer key.

## Try it

1. Install Ollama: https://ollama.com/download
2. Download the model once: `ollama run gemma3:1b`
3. Install Python dependencies: `python -m pip install -r requirements.txt`
4. Run the app: `streamlit run app.py`

The repository README contains the complete setup guide and troubleshooting steps.

## What I would improve next

I would like to add PDF support, a local history of generated study packs, and checks that help students compare generated answers with their original notes.

## Closing

LazyMate is a small experiment in using open-weight AI to give people back a little time. The goal is not to avoid learning; it is to spend less energy on repetitive formatting and more energy on understanding.

#devchallenge #hf26challenge
