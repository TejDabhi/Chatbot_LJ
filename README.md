# AIML_Tracking-Excel

A Python project for AI/ML tracking and Excel-based data processing.

---

# Prerequisites

Before getting started, ensure you have:

- Python 3.10 or later
- Git (optional, for cloning the repository)

---

# Installation

## 1. Install `uv`

### Windows (PowerShell)

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### macOS / Linux

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Verify the installation:

```bash
uv --version
```

---

## 2. Initialize the Project

```bash
uv init
```

---

## 3. Create a Virtual Environment

```bash
uv venv
```

This creates a `.venv` folder in your project.

---

## 4. Activate the Virtual Environment

### Windows (PowerShell)

```powershell
.venv\Scripts\activate
```

### Windows (Command Prompt)

```cmd
.venv\Scripts\activate.bat
```

### macOS / Linux

```bash
source .venv/bin/activate
```

Once activated, your terminal should display something similar to:

```text
(.venv)
```

---

## 5. Install Dependencies

If your project uses a `requirements.txt` file:

```bash
uv add -r requirements.txt
```

Alternatively, if your project already has a `pyproject.toml` and `uv.lock`:

```bash
uv sync
```

---

# Project Structure

```text
AIML_Tracking-Excel/
├── .venv/
├── requirements.txt
├── README.md
├── pyproject.toml
├── uv.lock
└── ...
```

---

# Running the Project

Run your application using:

```bash
uv run <your_script>.py
```

Example:

```bash
uv run main.py
```

You can also activate the virtual environment first and run Python directly:

```bash
python main.py
```

---

# Adding New Dependencies

Install a new package:

```bash
uv add <package-name>
```

Example:

```bash
uv add pandas
```

---

# Installing Dependencies Again

Using `requirements.txt`:

```bash
uv add -r requirements.txt
```

Or, if using `pyproject.toml`:

```bash
uv sync
```

---

# Updating Dependencies

Update all project dependencies:

```bash
uv lock --upgrade
uv sync
```

---

# Deactivating the Virtual Environment

When you're finished:

```bash
deactivate
```

---

# Notes

- `uv` automatically manages virtual environments and dependencies.
- Activate the virtual environment before running Python directly.
- If you use `uv run`, manual activation is not required.
- Commit the `uv.lock` file to ensure reproducible environments across different machines.
- The activation command differs between Windows and macOS/Linux:
  - Windows: `.venv\Scripts\activate`
  - macOS/Linux: `source .venv/bin/activate`
