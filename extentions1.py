file_name = input("Enter a file name: ").strip().lower()
    
extensionsmap = {
    ".gif": "image/gif",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
    ".pdf": "application/pdf",
    ".txt": "text/plain",
    ".zip": "application/zip"
}

for ext, mime in extensionsmap.items():
    if file_name.endswith(ext):
        print(mime)
        break
    else:
        print("application/octet-stream")
        break