# 🤖 ACD – Automatic Code Documentation

Welcome to **ACD (Auto Code Docs)** – an intelligent system that automatically generates beautiful, human-readable documentation for your Python code using powerful LLMs and deploys it to GitHub Pages.

## 📸 Project Preview
<p align="center"> <img src="docs/assets/screenshot.png" alt="Site Screenshot" width="80%" /> </p>

---

## 🎞️ Live Demo (GIF)

Here’s how the system works from code to docs!

<p align="center"> <img src="docs/assets/demo.gif" alt="Demo GIF" width="70%" /> </p>

---
## 📌 Overview

ACD (Automatic Code Documentation) is a smart system that uses an LLM (like CodeLlama) to analyze your Python source code and generate clean, readable Markdown documentation. This documentation is then published as a beautiful static site using MkDocs with the Material theme, and hosted for free via GitHub Pages.

<div align="center">
  <a href="https://aoeukun.github.io/ACD/">
    <img src="https://img.shields.io/badge/View-Docs-blue?style=flat-square" alt="View Docs">
  </a>
</div>

---

## ✨ Features

- 🧠 **LLM-based Documentation**  
  Uses [Ollama](https://ollama.com/) with [CodeLlama](https://huggingface.co/codellama) to understand and document your code.

- 🛠️ **Automatic Script**  
  A custom Python script `generate_docs.py` scans `.py` files and creates Markdown docs.

- 🌐 **Static Site Generator**  
  [MkDocs](https://www.mkdocs.org/) with the [Material theme](https://squidfunk.github.io/mkdocs-material/) for clean, modern UI.

- 🚀 **GitHub Actions CI/CD**  
  Documentation is regenerated and deployed automatically on each push.

- 📄 **Hosted on GitHub Pages**  
  Live documentation available here: [aoeukun.github.io/ACD](https://aoeukun.github.io/ACD/)

---

## 🗂️ Project Structure

ADC/
│
├── .github/workflows/deploy.yml   # GitHub Action for CI/CD
├── docs/
│   ├── index.md                   # Homepage content
│   └── generated/
│       ├── one.md                 # Generated docs from src/one.py
│       ├── two.md
│       └── three.md
├── site/                          # MkDocs build output (auto-generated)
├── src/
│   ├── one.py                     # Source code files
│   ├── two.py
│   └── three.py
├── venv/                          # Python virtual environment (optional)
├── generated_docs.py              # Main script for LLM-based documentation
├── mkdocs.yml                     # MkDocs configuration file
└── README.md                      # You're here!

---

## 🚀 Live Site
📄 https://aoeukun.github.io/ACD

Hosted via GitHub Pages and updated automatically on every push!

---
## 🛠️ How It Works

1. Write code in the src/ folder.
2. Run the generate_docs.py script to:

        -Extract functions, classes, and their descriptions using CodeLlama.
        -Create .md files under docs/generated/.

3. Markdown files are saved under `docs/generated/`.
4. MkDocs builds a static website from these files.
5. GitHub Actions deploys it automatically to GitHub Pages.

---

## 📦 Requirements

1. Python 3.8+
2. Ollama
3. CodeLlama model installed via Ollama
4. MkDocs & Material Theme

---


## 🚀 Getting Started (Locally)

1. **Clone the repo**
   ```bash
   git clone https://github.com/aoeukun/ACD.git
   cd ACD
2. **Install dependencies**
    pip install mkdocs mkdocs-material
3. **Start Ollama with CodeLlama**
    ollama run codellama
4. **Generate Docs**
    python generate_docs.py
5. **mkdocs serve**
    mkdocs serve
6. **🚀 Deploy to GitHub Pages**

On push, GitHub Actions will:
    Run generate_docs.py
    Build the MkDocs site
    Deploy to the gh-pages branch
