import os

import shutil
 
source_root = r"C:\Users\w10185657\OneDrive - The University of Southern Mississippi\695_Project_Thesis\YOLO_DeepSEA\Deepfish"

target_root = r"C:\Users\w10185657\OneDrive - The University of Southern Mississippi\695_Project_Thesis\YOLO_DeepSEA\dataset"
 
# Create YOLOv5 structure

for split in ['train', 'val']:

    os.makedirs(os.path.join(target_root, 'images', split), exist_ok=True)

    os.makedirs(os.path.join(target_root, 'labels', split), exist_ok=True)
 
# Flatten all 21 subfolders

for folder_name in os.listdir(source_root):

    folder_path = os.path.join(source_root, folder_name)

    if not os.path.isdir(folder_path):

        continue
 
    for split in ['train', 'valid']:

        split_path = os.path.join(folder_path, split)

        if not os.path.exists(split_path):

            continue
 
        for file in os.listdir(split_path):

            file_path = os.path.join(split_path, file)

            name, ext = os.path.splitext(file)

            dest_split = 'train' if split == 'train' else 'val'
 
            if ext.lower() == '.jpg':

                dest = os.path.join(target_root, 'images', dest_split, f"{folder_name}_{file}")

            elif ext.lower() == '.txt':

                dest = os.path.join(target_root, 'labels', dest_split, f"{folder_name}_{file}")

            else:

                continue
 
            shutil.copyfile(file_path, dest)

 