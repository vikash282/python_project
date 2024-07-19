import os
import shutil

def organize_files(directory):
    file_types = {
        'images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
        'videos': ['.mp4', '.mov', '.avi', '.mkv'],
        'music': ['.mp3', '.wav', '.aac'],
        'archives': ['.zip', '.rar', '.tar', '.gz'],
        'others': []
    }

    if not os.path.isdir(directory):
        return f"{directory} is not a valid directory."

    for category, extensions in file_types.items():
        folder_path = os.path.join(directory, category)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isfile(item_path):
            file_extension = os.path.splitext(item)[1].lower()
            moved = False
            for category, extensions in file_types.items():
                if file_extension in extensions:
                    shutil.move(item_path, os.path.join(directory, category, item))
                    moved = True
                    break
            if not moved:
                shutil.move(item_path, os.path.join(directory, 'others', item))
    
    return "Files organized successfully!"
