import os

for curr_dir,folders,files in os.walk('Training_Batch_Files'):
    for file in files:
        if file.endswith('.csv'):
            os.system(f"dvc add {os.path.join(curr_dir, file)}")

