from copystatic import copy_static
from gencontent import generate_pages_recursive


def main():
    src = "./static"
    dst = "./public"
    dir_src = "./content"
    template = "./template.html"
    dir_dst = "./public"

    copy_static(src, dst)
    generate_pages_recursive(dir_src, template, dir_dst)

if __name__ == "__main__":
    main()