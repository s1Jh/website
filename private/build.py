import markdown
import sys
import os
from mdx_gfm import GithubFlavoredMarkdownExtension
from configparser import ConfigParser
import copy
import shutil

default_vars = {}

def build_file(path: str):
    print(f"Processing {path}")
    markdown_text = ""
    replacements = copy.copy(default_vars)

    template = "$CONTENT$"

    with open(path, "r") as f:
        for line in f:
            if line.startswith("$$"):
                key = line[line.find("$$") + 2 : line.find(" ")]
                value = line[line.find(" ") + 1:-1]
                print(f"{key}: {value}")
                replacements[key] = value

            elif line.startswith("&&"):
                value = line[line.find("&&") + 2:-1]
                value = os.path.join("private/templates", value)
                if os.path.exists(value):
                    print(f"Template: {value}")
                    template_file = open(value, "r")
                    template = template_file.read()
                    template_file.close()
            else:
                markdown_text += line

    html_text = markdown.markdown(markdown_text, extensions=[GithubFlavoredMarkdownExtension()])
    template = template.replace("$CONTENT$", html_text)

    for replacement in replacements:
        template = template.replace(f"${replacement}$", replacements[replacement])

    this_path = os.getcwd()
    out_path = os.path.relpath(path, "./private")
    out_path = os.path.join(".", out_path)
    out_path = out_path.replace(".article", ".html")

    print(f"Out: {out_path}")

    os.makedirs(os.path.dirname(out_path), exist_ok=True)

    file_out = open(out_path, "w")
    file_out.write(template)
    file_out.close()

KEEP_DIRS = [
    "private",
    ".vscode",
    "img",
    ".git",
    "default.css",
    "styles.css",
    ".gitignore",
    "requirements.txt"
]

if __name__ == "__main__":
    config = ConfigParser()
    config.read("private/defaults.ini")


    for option in config.options("DEFAULTS"):
        default_vars[option.upper()] = config.get("DEFAULTS", option)

    for file in os.listdir("."):
        if file not in KEEP_DIRS:
            delete_path = os.path.join('.', file)
            print(f"Deleting {delete_path}")
            if os.path.isdir(delete_path):
                shutil.rmtree(delete_path)
            else:
                os.remove(delete_path)

    for dirpath, dirnames, filenames in os.walk("private/"):
        for filename in filenames:
            path = os.path.join(dirpath, filename)

            fname = os.path.basename(path)

            if ".article" in path and not fname.startswith("-"):
                build_file(path)

