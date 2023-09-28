import os

def rm(filename):
    try:
        os.remove(filename)
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{filename}' not found.")
