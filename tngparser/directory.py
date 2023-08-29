from typing import List, Optional
import os
import glob

def get_files(dir_path: str, search_pattern: Optional[str] = None) -> List[str]:
    if search_pattern is None:
        file_list = []
        for entry in os.listdir(dir_path):
            full_path = os.path.join(dir_path, entry)
            if os.path.isfile(full_path):
                file_list.append(full_path)
        return file_list
    else:
        pattern = os.path.join(dir_path, search_pattern)
        file_list = glob.glob(pattern)
        return file_list