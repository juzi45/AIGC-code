import os
import shutil

def copy_media_files(m3u8_file_path):
    media_folder_path = os.getcwd()
    with open(m3u8_file_path, 'r',encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith('#'):
                continue
            media_file_path = os.path.join(os.path.dirname(m3u8_file_path), line.strip())
            if os.path.exists(media_file_path):
                media_file_name = os.path.basename(media_file_path)
                media_file_extension = os.path.splitext(media_file_name)[1]
                media_file_new_path = os.path.join(media_folder_path, media_file_name)
                if os.path.exists(media_file_new_path):
                    print(f"{media_file_new_path} already exists")
                else:
                    shutil.copy(media_file_path, media_file_new_path)
                    print(f"Copied {media_file_path} to {media_file_new_path}")
            else:
                print(f"{media_file_path} does not exist")

# Example usage
m3u8_file_path = './path/file.m3u8'
copy_media_files(m3u8_file_path)
