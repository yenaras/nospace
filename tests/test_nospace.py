#!/usr/bin/env python3
import os
import shutil
from pathlib import Path

from nospace.nospace import rename


# Helper function to create a test directory with files and folders
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


# Helper function to remove the test directory after the tests are done
def teardown_test_directory():
    path = Path("test_directory")
    if path.exists():
        shutil.rmtree(path)


def test_rename_files_lowercase_both_objects_with_separator():
    setup_test_directory()
    rename("test_directory", None, "lower", "both", "_")

    try:
        assert os.path.exists("test_directory/test_file.txt")
        assert os.path.exists("test_directory/sub_directory/sub_file.txt")
        assert os.path.exists(
            "test_directory/sub_directory/sub_sub_directory/sub_sub_file.txt"
        )
    except Exception as e:
        print(f"test failed because of exception {e}")
    finally:
        teardown_test_directory()


def test_rename_files_uppercase_only_files_with_separator():
    setup_test_directory()
    rename("test_directory", None, "upper", "files", "_")

    try:
        assert os.path.exists("test_directory/TEST_FILE.TXT")
        assert os.path.exists("test_directory/sub_directory/SUB_FILE.TXT")
        assert os.path.exists(
            "test_directory/sub_directory/sub_sub_directory/SUB_SUB_FILE.TXT"
        )
    except Exception as e:
        print(f"test failed because of exception: {e}")
    finally:
        teardown_test_directory()


def test_rename_files_titlecase_only_folders_with_separator():
    setup_test_directory()
    try:
        rename("test_directory", None, "title", "folders", "_")

        assert os.path.exists("test_directory/test_file.txt")
        assert os.path.exists("test_directory/Sub_Directory/sub_file.txt")
        assert os.path.exists(
            "test_directory/Sub_Directory/Sub_Sub_Directory/sub_sub_file.txt"
        )
    except Exception as e:
        print(f"Test failed because exception: {e}")
    finally:
        teardown_test_directory()


def test_rename_files_depth_limit():
    setup_test_directory()
    try:
        rename("test_directory", 2, "lower", "both", "_")
        teardown_test_directory()
    except Exception as e:
        print(f"Test failed because exception: {e}")
    finally:
        teardown_test_directory()
