import os
import random

class WinShredder:
    def __init__(self, file_path):
        self.file_path = file_path

    def shred_file(self):
        """Shred the file by overwriting it with random data."""
        if not os.path.exists(self.file_path):
            print(f"File {self.file_path} does not exist.")
            return
        
        try:
            # Get the size of the file
            file_size = os.path.getsize(self.file_path)
            print(f"Shredding file of size: {file_size} bytes")

            # Overwrite the file with random data multiple times
            with open(self.file_path, 'r+b') as f:
                for i in range(3):  # Three-pass overwriting
                    print(f"Overwriting pass {i + 1}")
                    f.seek(0)
                    random_data = os.urandom(file_size)
                    f.write(random_data)
                    f.flush()
                    os.fsync(f.fileno())
            
            # Rename the file to something random
            random_name = os.urandom(16).hex()
            os.rename(self.file_path, random_name)

            # Finally delete the file
            os.remove(random_name)
            print(f"File {self.file_path} has been securely shredded.")
        
        except Exception as e:
            print(f"An error occurred: {e}")

def main():
    file_path = input("Enter the path of the file to shred: ")
    shredder = WinShredder(file_path)
    shredder.shred_file()

if __name__ == "__main__":
    main()