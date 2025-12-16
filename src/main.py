from copystatic import copy_static


def main():
    src = "./static"
    dst = "./public"

    copy_static(src, dst)


if __name__ == "__main__":
    main()