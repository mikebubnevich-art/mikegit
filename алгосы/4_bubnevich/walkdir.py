import sys
import os

def walk_directory(path, root_path, files):
    try:
        items = os.listdir(path)
    except PermissionError:
        return
    
    for item in items:
        item_path = path + os.sep + item
        if os.path.isdir(item_path):
            walk_directory(item_path, root_path, files)
        elif os.path.isfile(item_path):
            size = os.stat(item_path).st_size
           
            rel_path = item_path[len(root_path) + 1:]
            files.append((size, rel_path))

def main():
    if len(sys.argv) != 2:
        return
    
    root_path = sys.argv[1]
    
    if not os.path.isdir(root_path):
        return
    
    files = []
    walk_directory(root_path, root_path, files)
    
    
    files.sort(key=lambda x: x[0], reverse=True)
    
   
    top5 = files[:5]
    
    
    result = []
    for size, rel_path in top5:
        if size < 1024 * 1024:
            formatted = round(size / 1024, 2)
        else:
            formatted = round(size / (1024 * 1024), 2)
        result.append((formatted, rel_path))
    
   
    print(len(files))
    print(result)

if __name__ == "__main__":
    main()