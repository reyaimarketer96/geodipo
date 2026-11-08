import zipfile
import os

BUNDLE_NAME = "geodipo_rag_worker.zip"

files_to_include = [
    "server_worker.py",
    "checkpoint.json",
    "run.sh",
    "monitor.sh",
    "status.sh",
    "stop.sh"
]

dirs_to_include = [
    "rag_knowledge_base"
]

print(f"Creating {BUNDLE_NAME}...")
with zipfile.ZipFile(BUNDLE_NAME, "w", zipfile.ZIP_DEFLATED) as zipf:
    for f in files_to_include:
        if os.path.exists(f):
            print(f"Adding file: {f}")
            zipf.write(f, arcname=f)
        else:
            print(f"Warning: File {f} does not exist!")

    for d in dirs_to_include:
        for root, dirs, files in os.walk(d):
            # Skip __pycache__
            if "__pycache__" in root:
                continue
            for file in files:
                file_path = os.path.join(root, file)
                print(f"Adding: {file_path}")
                zipf.write(file_path, arcname=file_path)

size_mb = os.path.getsize(BUNDLE_NAME) / (1024 * 1024)
print(f"Successfully packaged {BUNDLE_NAME} ({size_mb:.2f} MB)!")
