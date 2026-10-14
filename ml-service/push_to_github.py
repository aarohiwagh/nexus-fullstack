"""
Helper script to push all changes directly to GitHub via GitHub REST API.
Usage:
    python push_to_github.py <YOUR_GITHUB_PERSONAL_ACCESS_TOKEN>
"""
import sys
import os
import base64
import requests
from pathlib import Path

REPO_OWNER = "shivamubarhande60-cell"
REPO_NAME = "nexus-ml"
BRANCH = "main"
BASE_DIR = Path(__file__).resolve().parent

IGNORE_DIRS = {"venv", ".git", "__pycache__", ".idea", ".vscode"}
IGNORE_EXTS = {".pyc", ".pyo", ".zip"}


def upload_files(token: str):
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    print(f"Uploading files to https://github.com/{REPO_OWNER}/{REPO_NAME} (branch: {BRANCH})...")

    for root, dirs, files in os.walk(BASE_DIR):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        for f in files:
            file_path = Path(root) / f
            if file_path.suffix in IGNORE_EXTS:
                continue

            rel_path = file_path.relative_to(BASE_DIR).as_posix()
            
            # Skip push helper itself
            if f == "push_to_github.py":
                continue

            with open(file_path, "rb") as fp:
                content_bytes = fp.read()
            encoded_content = base64.b64encode(content_bytes).decode("utf-8")

            url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{rel_path}"
            
            # Check if file already exists on GitHub to obtain its SHA
            get_res = requests.get(url, headers=headers, params={"ref": BRANCH})
            sha = get_res.json().get("sha") if get_res.status_code == 200 else None

            payload = {
                "message": f"feat: add {rel_path} for screening intelligence service",
                "content": encoded_content,
                "branch": BRANCH
            }
            if sha:
                payload["sha"] = sha

            put_res = requests.put(url, headers=headers, json=payload)
            if put_res.status_code in [200, 201]:
                print(f" [OK] {rel_path}")
            else:
                print(f" [ERR] {rel_path} -> {put_res.status_code}: {put_res.text}")

    print("\n[COMPLETE] All files uploaded to GitHub successfully!")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python push_to_github.py <GITHUB_TOKEN>")
        sys.exit(1)
    upload_files(sys.argv[1])
