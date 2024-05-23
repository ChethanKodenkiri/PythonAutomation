
import sys
from behave import __main__ as behave_main

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python test_runner.py <feature_file_path>")
        sys.exit(1)

    feature_file_path = sys.argv[1]
    behave_main.main([feature_file_path])