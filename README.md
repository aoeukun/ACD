# 🤖 ACD – Automatic Code Documentation

Welcome to **ACD (Auto Code Docs)** – an intelligent system that automatically generates beautiful, human-readable documentation for your Python code using powerful LLMs and deploys it to GitHub Pages.

<div align="center">
  <img src="https://img.shields.io/github/deployments/aoeukun/ACD/github-pages?label=GitHub%20Pages&style=flat-square" alt="GitHub Pages Status"/>
  <a href="https://aoeukun.github.io/ACD/">
    <img src="https://img.shields.io/badge/View-Docs-blue?style=flat-square" alt="View Docs">
  </a>
</div>

---

## 📌 Features

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




---

## ⚙️ How It Works

1. `generate_docs.py` reads `.py` files from `src/`.
2. It sends code to **CodeLlama** via Ollama and receives back clean Markdown docs.
3. Markdown files are saved under `docs/generated/`.
4. MkDocs builds a static website from these files.
5. GitHub Actions deploys it automatically to GitHub Pages.

---

## 🚀 Getting Started (Locally)

1. **Clone the repo**
   ```bash
   git clone https://github.com/aoeukun/ACD.git
   cd ACD
