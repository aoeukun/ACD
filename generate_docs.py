import subprocess
from pathlib import Path

SYSTEM_PROMPT = (
    "You are a helpful assistant that generates markdown documentation "
    "for Python code. For each function/class/module, provide a clear "
    "description, input/output details, and usage example if applicable."
    "Generate documentation in markdown for the following Python file. Include descriptions of all functions, classes, arguments, and return types. Use headings and lists where appropriate."

"```python"
# code here

)

def call_ollama(prompt: str, model="codellama"):
    result = subprocess.run(
        ["ollama", "run", model],
        input=prompt.encode("utf-8"),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return result.stdout.decode("utf-8")

def generate_docs_from_code_file(code_path: Path, output_dir: Path):
    with open(code_path, "r", encoding="utf-8") as f:
        code = f.read()

    prompt = f"{SYSTEM_PROMPT}\n\n```python\n{code}\n```"
    docs = call_ollama(prompt)

    output_file = output_dir / f"{code_path.stem}.md"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"# Documentation for `{code_path.name}`\n\n")
        f.write(docs)

def main():
    src_dir = Path("src")
    output_dir = Path("docs/generated")
    output_dir.mkdir(parents=True, exist_ok=True)

    for py_file in src_dir.rglob("*.py"):
        generate_docs_from_code_file(py_file, output_dir)

if __name__ == "__main__":
    main()

import os

def update_index():
    doc_files = [f for f in os.listdir("docs") if f.endswith(".md") and f != "index.md"]
    with open("docs/index.md", "w", encoding="utf-8") as index_file:
        index_file.write("# 📚 Code Documentation Index\n\n")
        index_file.write("Generated documentation files:\n\n")
        for doc in sorted(doc_files):
            name = os.path.splitext(doc)[0].replace("_", " ").title()
            index_file.write(f"- [{name}]({doc})\n")

update_index()

