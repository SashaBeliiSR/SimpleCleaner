import os
import shutil

def get_folder_size(folder):
    total_size = 0
    for dirpath, _, filenames in os.walk(folder):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            if os.path.isfile(filepath):
                total_size += os.path.getsize(filepath)
    return total_size // (1024 * 1024 * 1024)  # Size in GB

def clear_folder(folder):
    for item in os.listdir(folder):
        item_path = os.path.join(folder, item)
        try:
            if os.path.isfile(item_path) or os.path.islink(item_path):
                os.remove(item_path)
                print(f"Deleted file: {item_path}")
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)
                print(f"Deleted folder: {item_path}")
        except Exception as e:
            print(f"Could not delete {item_path}: {e}")

def clear_trash():
    try:
        import ctypes
        ctypes.windll.shell32.SHEmptyRecycleBinW(None, None, 0)
        print("Recycle Bin cleared.")
    except Exception as e:
        print(f"Could not clear Recycle Bin: {e}")

def main():
    temp_folder = os.environ.get("TEMP")
    downloads_folder = os.path.expanduser("~/Downloads")
    trash_folder = os.path.join(os.environ.get("SYSTEMDRIVE"), "$Recycle.Bin")

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("===========================")
        print("         Cleaner")
        print("===========================")

        temp_size = get_folder_size(temp_folder)
        downloads_size = get_folder_size(downloads_folder)
        trash_size = get_folder_size(trash_folder)

        print(f"\nTemp folder: {temp_size} GB")
        print(f"Downloads folder: {downloads_size} GB")
        print(f"Recycle Bin: {trash_size} GB")
        print("\nCommands:")
        print("t - Clear Temp")
        print("d - Clear Downloads")
        print("b - Clear Recycle Bin")
        print("e - Exit")
        print()

        choice = input("Enter command: ").strip().lower()

        if choice == 't':
            clear_folder(temp_folder)
        elif choice == 'd':
            clear_folder(downloads_folder)
        elif choice == 'b':
            clear_trash()
        elif choice == 'e':
            print("Exiting...")
            break
        else:
            print("Invalid command. Try again.")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
