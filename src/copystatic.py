import os
import shutil

def copy_static(src, dst):
    if os.path.exists(dst):
        print(f"Deleting old directory: {dst}")
        shutil.rmtree(dst)
    
    os.mkdir(dst)
    _copy_recursive(src, dst)
    
def _copy_recursive(src, dst):    
    
    content = os.listdir(src)
    for file in content:
        src_path = os.path.join(src, file)
        dst_path = os.path.join(dst, file)
        
        if os.path.isfile(src_path):
            print(f"Copying file: {src_path} -> {dst_path}")
            shutil.copy(src_path, dst_path)
        else:
            print(f"Creating directory: {dst_path}")
            os.mkdir(dst_path)
            _copy_recursive(src_path, dst_path)
