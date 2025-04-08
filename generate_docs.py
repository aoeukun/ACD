import subprocess
from pathlib import Path
import os
import yaml

# 📌 System prompt to guide the LLM (CodeLlama via Ollama)
SYSTEM_PROMPT = (
    "You are a helpful assistant that generates markdown documentation for Python code. For each function/class/module, provide a clear description, input/output details, and usage example if applicable."
    "Generate documentation in markdown for the following Python file. "
    "Include descriptions of all functions, classes, arguments, and return types. "
    "Use headings and lists where appropriate."
)

# 🧠 Function to call Ollama with a prompt
def call_ollama(prompt: str, model="codellama"):
    result = subprocess.run(
        ["ollama", "run", model],
        input=prompt.encode("utf-8"),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return result.stdout.decode("utf-8")

# 📄 Convert a .py file into a .md file using LLM
def generate_docs_from_code_file(code_path: Path, output_dir: Path):
    with open(code_path, "r", encoding="utf-8") as f:
        code = f.read()

    prompt = f"{SYSTEM_PROMPT}\n\n```python\n{code}\n```"
    docs = call_ollama(prompt)

    output_file = output_dir / f"{code_path.stem}.md"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"# Documentation for `{code_path.name}`\n\n")
        f.write(docs)

# 🔁 Scan all .py files in src/ and generate docs
def generate_all_docs():
    src_dir = Path("src")
    output_dir = Path("docs/generated")
    output_dir.mkdir(parents=True, exist_ok=True)

    for py_file in src_dir.rglob("*.py"):
        generate_docs_from_code_file(py_file, output_dir)

# 🧭 Automatically update mkdocs.yml with the generated .md files
def update_mkdocs_yml():
    GENERATED_DIR = "docs/generated"
    MKDOCS_YML_PATH = "mkdocs.yml"

    with open(MKDOCS_YML_PATH, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    # Filter only relevant .md files
    files = [f for f in os.listdir(GENERATED_DIR) if f.endswith(".md") and f != "docs.md"]
    files.sort()

    # Rebuild the 'nav' section
    new_nav = []
    for item in config.get("nav", []):
        if isinstance(item, dict) and "Generated Docs" in item:
            continue
        new_nav.append(item)

    generated_section = {"Generated Docs": []}
    for file in files:
        title = file[:-3].title()
        generated_section["Generated Docs"].append({title: f"generated/{file}"})

    new_nav.append(generated_section)
    config["nav"] = new_nav

    with open(MKDOCS_YML_PATH, "w", encoding="utf-8") as f:
        yaml.dump(config, f, sort_keys=False)

    print("✅ mkdocs.yml sidebar updated.")

# 🚀 Main entrypoint: generate docs and update mkdocs nav
if __name__ == "__main__":
    generate_all_docs()
    update_mkdocs_yml()
    print("🎉 Documentation generated and mkdocs.yml updated.")
