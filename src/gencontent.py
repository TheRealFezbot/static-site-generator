import os
from pathlib import Path
from block_markdown import markdown_to_html_node




def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    

    with open(from_path, "r") as f:
        md = f.read()
    with open(template_path, "r") as f:
        template = f.read()

    title = extract_title(md)
    content = markdown_to_html_node(md).to_html()

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", content)

    dest_dir = os.path.dirname(dest_path)
    os.makedirs(dest_dir, exist_ok=True)

    with open(dest_path, "w") as f:
        f.write(template)


def extract_title(markdown):
    split_lines = markdown.split("\n")

    for line in split_lines:
        if line.startswith("# "):
            return line[2:].strip()
            
    raise Exception("No title found")

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    dirs = os.listdir(dir_path_content)

    for dir in dirs:
        dir_path = os.path.join(dir_path_content, dir)
        dest_path = os.path.join(dest_dir_path, dir)
        if os.path.isfile(dir_path):
            dest_html_path = Path(dest_path).with_suffix(".html")
            generate_page(dir_path, template_path, dest_html_path)
        elif os.path.isdir(dir_path):
            generate_pages_recursive(dir_path, template_path, dest_path)

