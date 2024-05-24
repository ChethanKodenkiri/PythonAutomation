
# import sys
# from behave import __main__ as behave_main
#
# if __name__ == "__main__":
#     if len(sys.argv) < 2:
#         print("Usage: python test_runner.py <feature_file_path>")
#         sys.exit(1)
#
#     feature_file_path = sys.argv[1]
#     behave_main.main([feature_file_path])

from behave.__main__ import main as behave_main
import os

if __name__ == "__main__":
    # Run Behave tests programmatically
    behave_args = ["features/soleOnboarding_feature.feature"]
    behave_args.extend(["--format", "allure_behave.formatter:AllureFormatter"])
    behave_args.extend(["--outfile", "reports/"])
    behave_main(behave_args)

    # Generate Allure report
    #os.system("allure serve reports/")