import shutil
from pathlib import Path

EXTENSIONS_MAP = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.csv', '.pptx'],
    'Scripts': ['.py', '.js', '.html', '.css'],
    'Audio': ['.mp3', '.wav', '.flac'],
    'Videos': ['.mp4', '.avi', '.mov']
}

def organize_directory(target_path_string):
    target_dir = Path(target_path_string)
    
    if not target_dir.exists():
        print(f"Error: The directory '{target_dir}' does not exist")
        return
    
    print(f"Scanning directory: {target_dir}")
    
    for item in target_dir.iterdir():
        if not item.is_file():
            continue
        
        file_extension = item.suffix.lower()
        
        destination_folder_name = 'hii'
        
        for category, extensions_list in EXTENSIONS_MAP.items():
            if file_extension in extensions_list:
                destination_folder_name = category
                break
            
            destination_dir = target_dir / destination_folder_name
            destination_dir.mkdir(exist_ok=True)
            destination_file_path = destination_dir / item.name
            
            try:
                shutil.move(str(item), str(destination_file_path))
                print(f'Moved: {item.name} -> {destination_folder_name}')
            except Exception as e:
                print(f'Error moving {item.name}: {e}')
                
if __name__ == '__main__':
    folder_to_organize = "./messy_folder"

    organize_directory(folder_to_organize)
    print("Organization complete!")