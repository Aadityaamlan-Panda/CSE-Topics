import os

# Path to the folder containing the images
folder_path = r"."  # <-- change this to your folder

# Loop through the slide numbers
for i in range(1, 116):  # 1 to 115
    old_name = f"ChemE_Memory_Palace_V2_latest - {i:03}.jpg"  # 001, 002, ..., 115
    new_name = f"Slide{i}.jpg"
    
    old_path = os.path.join(folder_path, old_name)
    new_path = os.path.join(folder_path, new_name)
    
    # Check if the old file exists
    if os.path.exists(old_path):
        os.rename(old_path, new_path)
        print(f"Renamed: {old_name} -> {new_name}")
    else:
        print(f"File not found: {old_name}")
