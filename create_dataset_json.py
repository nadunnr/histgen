import json
import random

# --- CONFIGURATION ---
# Input: Use the partial file we fixed earlier (since it matches your disk)
input_path = "/home/nadun/wd/datasets/histgen_data/annotation_partial.json" 
# Output: The new mini file
output_path = "dataset_annotations.json"
# Percentage to keep (0.1 = 10%)
fraction = 0.1
# ---------------------

print(f"Loading from {input_path}...")
with open(input_path, 'r') as f:
    data = json.load(f)

new_data = {"train": [], "val": [], "test": []}

print("-" * 30)
for split in ["train", "val", "test"]:
    original_list = data[split]
    total_count = len(original_list)
    
    # Calculate how many items to keep
    keep_count = int(total_count * fraction)
    
    # Randomly sample unique items (no duplicates)
    mini_list = random.sample(original_list, keep_count)
    new_data[split] = mini_list
    
    print(f"Split '{split}': Reduced from {total_count} -> {keep_count} images")

print("-" * 30)
with open(output_path, 'w') as f:
    json.dump(new_data, f, indent=4)

print(f"SUCCESS! Saved dataset to: {output_path}")