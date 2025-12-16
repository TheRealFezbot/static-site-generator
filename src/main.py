from copystatic import copy_static
from gencontent import generate_page


def main():
    src = "./static"
    dst = "./public"
    page_src = "./content/index.md"
    template = "./template.html"
    page_dst = "./public/index.html"

    copy_static(src, dst)
    generate_page(page_src, template, page_dst)

if __name__ == "__main__":
    main()