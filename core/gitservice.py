import os
import subprocess

def clone_repo(git_url, destination):
    if not os.path.exists(destination):
        os.makedirs(destination)
    subprocess.check_call(["git", "clone", git_url], cwd=destination)
