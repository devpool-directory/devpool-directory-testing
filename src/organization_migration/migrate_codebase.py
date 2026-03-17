import os
import shutil

# This script helps migrate and refactor code to the new organization structure.

def migrate_codebase(src_dir, dest_dir):
    """Migrate code from old organization to new one"""
    # Ensure source and destination directories exist
    if not os.path.exists(src_dir):
        raise FileNotFoundError(f'Source directory {src_dir} not found')
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Iterate through the files in the source directory and migrate them
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            file_path = os.path.join(root, file)
            # Skip any files that are not relevant (e.g., read-only files)
            if file.endswith('.md') or 'README' in file:
                continue

            # Create the corresponding directory in the destination if it doesn't exist
            relative_path = os.path.relpath(file_path, src_dir)
            destination_file_path = os.path.join(dest_dir, relative_path)
            destination_dir = os.path.dirname(destination_file_path)

            if not os.path.exists(destination_dir):
                os.makedirs(destination_dir)

            # Copy the file to the new destination
            shutil.copy(file_path, destination_file_path)

            print(f'Migrated: {file_path} to {destination_file_path}')

if __name__ == '__main__':
    source_directory = os.getenv('OLD_ORG_SRC_PATH')
    destination_directory = os.getenv('NEW_ORG_DEST_PATH')

    if not source_directory or not destination_directory:
        raise ValueError('Source and destination directories must be provided via environment variables.')

    migrate_codebase(source_directory, destination_directory)
