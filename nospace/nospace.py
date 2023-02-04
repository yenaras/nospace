#!/usr/bin/env python3
import os
import argparse

parser = argparse.ArgumentParser(
    description="rename files in bulk to remove spaces")

parser.add_argument(
    "-d", "--depth", type=int, default=None,
    help="maximum depth of folders to traverse"
)
parser.add_argument(
    "-c",
    "--case",
    type=str,
    default="lower",
    choices=["lower", "title", "upper"],
    help="case of the renamed files and folders (lower, title, or upper)",
)
parser.add_argument(
    "-o",
    "--objects",
    type=str,
    default="both",
    choices=["both", "files", "folders"],
    help="objects to process (files, folders, or both)",
)
parser.add_argument(
    "-s", "--seperator", type=str, default="_",
    help="separator to replace spaces with (default is _)"
)
parser.add_argument(
    "-p", "--path", type=str, default=os.getcwd(),
    help="optional file path to start with"
)
args = parser.parse_args()


def main():
    rename(args.path, args.depth, args.case, args.objects, args.seperator)


def rename(parent, max_depth, case, objects, seperator):
    current_depth = parent.count(os.sep)

    if max_depth is not None and current_depth >= max_depth:
        return

    for path, folders, files in os.walk(parent):
        if objects in ['both', 'files']:
            for f in files:
                new_name = f.replace(" ", seperator)
                if case == "title":
                    new_name = new_name.title()
                elif case == "upper":
                    new_name = new_name.upper()
                else:
                    new_name = new_name.lower()

                old_path = os.path.join(path, f)
                new_path = os.path.join(path, new_name)

                os.rename(old_path, new_path)
                # os.remove(old_path)

        if objects in ['both', 'files']:
            for i in range(len(folders)):
                new_name = folders[i].replace(" ", seperator)
                if case == "title":
                    new_name = new_name.title()
                elif case == "upper":
                    new_name = new_name.upper()
                else:
                    new_name = new_name.lower()

                old_path = os.path.join(path, folders[i])
                new_path = os.path.join(path, new_name)
                os.rename(old_path, new_path)
                # os.remove(old_path)

                folders[i] = new_name

        if max_depth is None:
            continue

        for folder in folders:
            folder_path = os.path.join(path, folder)
            if folder_path.count(os.sep) >= max_depth:
                continue

            rename(folder_path, max_depth, case)


if __name__ == "__main__":
    main()
