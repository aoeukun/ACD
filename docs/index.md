# 🤖 Automatic Code Documentation

Welcome to **Auto Code Docs** — where your code meets intelligence.

Imagine a world where your Python codebase *documents itself* — beautifully, intelligently, and automatically. That's what we built. Sit back and let AI do the heavy lifting while you focus on creating brilliant software.

---

## ✨ Why This Project?

<br>
 🔥 **"90% Of developers hate writing docs. The other 10% are lying." – Every Developer Ever**

<br>
Writing documentation is tedious. But it's essential for collaboration, onboarding, and maintaining high-quality software. So we asked:

> **What if your code could explain itself?**

This project answers that with a seamless pipeline that **analyzes your code using an LLM**, extracts meaningful descriptions, and turns it all into a **fully-deployed website** — without you writing a single docstring.

---

## 🌟 Features You'll Love

- 🧠 **AI-Powered Clarity**  
  Uses [Ollama](https://ollama.com/) + CodeLlama to analyze your code and generate intelligent documentation.

- 🛠️ **Seamless Automation**  
  Set it and forget it — every push to GitHub triggers automatic doc generation and deployment.

- 📚 **Beautiful MkDocs Site**  
  Clean, responsive, and easy to navigate. Built with [MkDocs](https://www.mkdocs.org/) and deployed with GitHub Pages.

- 🚀 **Lightning-Fast Setup**  
  Drop in your code, run `generate_docs.py`, and you’re done. It's that easy.

---

## 🧠 How It Works (Behind the Magic)

1. **Code Analysis**  
   Scans your `.py` files and extracts all functions and classes.

2. **AI-Powered Description**  
   Sends the extracted code to an LLM locally via [Ollama](https://ollama.com/), which returns clean, natural-language descriptions.

3. **Markdown Generation**  
   The documentation is converted into `.md` files stored under `docs/generated/`.

4. **Site Build & Deployment**  
   Using MkDocs + GitHub Actions, the site is built and deployed — all in one click.

---

## 📂 Explore the Docs

Navigate through:

- 🔍 Function & Class descriptions
- 🧾 Auto-generated Markdown files
- 🧱 Project architecture

---


## 🛠 Tech Stack

| Tool         | Purpose                        |
|--------------|--------------------------------|
| 🧠 Ollama + CodeLlama | LLM for doc generation        |
| 🐍 Python     | Script for parsing and generation |
| 📘 MkDocs     | Static site generator          |
| 🛸 GitHub Actions | Automated deployment         |
| 🔵 VS Code    | Code editor                    |

---


## ❤️ Made With Passion

This project isn’t just about automation — it’s about **empowering developers** to write less and deliver more.

> Because when your code can speak for itself... you just code.

---
<div style="text-align: right; font-style: italic; color: gray; font-size: 0.9em;">
  — Created by S.Sandeep Kumar
</div>
