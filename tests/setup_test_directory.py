#!/usr/bin/env python3
import os
import sys
sys.dont_write_bytecode = True


def main():
    setup_test_directory()


def setup_test_directory():
    os.makedirs("test_directory/SUB DIRECTORY/SUB SUB DIRECTORY", exist_ok=True)
    with open("test_directory/TEST FILE.txt", "w") as f:
        f.write("test")
    with open("test_directory/SUB DIRECTORY/SUB FILE.txt", "w") as f:
        f.write("test")
    with open(
        "test_directory/SUB DIRECTORY/SUB SUB DIRECTORY/SUB SUB FILE.txt", "w"
    ) as f:
        f.write("test")


if __name__ == '__main__':
    main()
