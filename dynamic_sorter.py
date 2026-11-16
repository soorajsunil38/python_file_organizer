import shutil
from pathlib import Path

def hybrid_organizer(target_path_string):
    CATEGORY_MAP = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.svg', '.webp'],
        'Audio': ['.mp3', '.wav', '.flac', '.m4a', '.aac'],
        'Video': ['.mp4', '.mkv', '.avi', '.mov', '.wmv'],
        'Documents': ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.pptx', '.csv'],
        'Archives': ['.zip', '.rar', '.tar', '.gz', '.7z']
    }

    extension_to_category = {}
    for category, extensions in CATEGORY_MAP.items():
        for ext in extensions:
            extension_to_category[ext] = category

    target_dir = Path(target_path_string)

    if not target_dir.exists():
        print(f"Error: The directory '{target_dir}' does not exist.")
        return

    print(f"Scanning directory: {target_dir}")

    for item in target_dir.iterdir():
        if not item.is_file():
            continue
            
        file_extension = item.suffix.lower()
        
        if not file_extension:
            destination_folder_name = "Others"
            
        elif file_extension in extension_to_category:
            destination_folder_name = extension_to_category[file_extension]
            
        else:
            clean_name = file_extension.replace('.', '').upper()
            destination_folder_name = f"{clean_name}_Files"

        destination_dir = target_dir / destination_folder_name
        destination_dir.mkdir(exist_ok=True)
        
        destination_file_path = destination_dir / item.name
        
        try:
            shutil.move(str(item), str(destination_file_path))
            print(f"Moved: {item.name} -> {destination_folder_name}/")
        except Exception as e:
            print(f"Could not move {item.name}. Reason: {e}")

if __name__ == "__main__":
    folder_to_organize = "./messy_folder2" 
    
    hybrid_organizer(folder_to_organize)
    print("Hybrid organization complete!")