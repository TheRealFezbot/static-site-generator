import sys
from copystatic import copy_static
from gencontent import generate_pages_recursive


def main():
    if len(sys.argv) == 1:
        basepath = "/"
    else:
        basepath = sys.argv[1]
    src = "./static"
    dst = "./docs"
    dir_src = "./content"
    template = "./template.html"
    dir_dst = "./docs"

    copy_static(src, dst)
    generate_pages_recursive(basepath, dir_src, template, dir_dst)

if __name__ == "__main__":
    main()