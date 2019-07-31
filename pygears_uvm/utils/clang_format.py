import os
import subprocess

def clang_format(dir):
    dir = os.path.abspath(dir)
    for root, dirs, files in os.walk(dir):
        for file in files:
            file = os.path.join(root, file)
            if file.endswith(".hpp") or file.endswith(".cpp"):
                subprocess.check_call(['clang-format', '-i', file])
