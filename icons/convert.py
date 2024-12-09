import os
import time
from PIL import Image
from colorama import Back, Fore, Style, init

# Initialize colorama
init(autoreset=True)

version = "2.7.5"

def clear():
    """Clear the terminal screen."""
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Unix-based systems like Linux and macOS
        os.system('clear')

def convert_ico_to_png(source_dir, output_dir):
    """
    Traverse the source directory and convert all .ico files to .png, 
    preserving the folder structure in the output directory.
    """
    for root, _, files in os.walk(source_dir):
        for file in files:
            if file.endswith('.ico'):
                ico_path = os.path.join(root, file)
                
                # Compute relative path and target folder in the output directory
                relative_path = os.path.relpath(root, source_dir)
                target_folder = os.path.join(output_dir, relative_path)
                os.makedirs(target_folder, exist_ok=True)

                # Create the full path for the .png file
                png_path = os.path.join(target_folder, file.replace('.ico', '.png'))
                
                try:
                    # Convert .ico to .png and save
                    with Image.open(ico_path) as img:
                        img.save(png_path, format='PNG')
                    print(f"{Back.WHITE}{Fore.BLACK}Converted{Style.RESET_ALL}: {ico_path} -> {png_path}")
                except Exception as e:
                    print(f"{Back.RED}Failed to convert{Style.RESET_ALL} {ico_path}: {e}")

def count_files_with_extension(directory, extension):
    """
    Count all files with the specified extension in the directory and its subdirectories.
    """
    count = 0
    for root, _, files in os.walk(directory):
        count += sum(1 for file in files if file.endswith(extension))
    return count

if __name__ == "__main__":
    # Clear the terminal
    clear()

    # Prints about script
    print(f"\n{Back.WHITE}{Fore.BLACK}si9598{Style.RESET_ALL} | {Back.YELLOW}{Fore.BLACK}{version}{Style.RESET_ALL}\n")

    # Wait for 2.5 seconds
    time.sleep(2.5)

    # Prints elipsy warning
    print(f"\n{Back.WHITE}{Fore.BLACK}Epilepsy{Style.RESET_ALL} {Back.YELLOW}{Fore.BLACK}Warning{Style.RESET_ALL}\n")

    # Wait for 10 seconds
    time.sleep(10)

    # Define directories
    ico_directory = "ico-files"
    png_directory = "png-files"
    
    # Ensure output directory exists
    os.makedirs(png_directory, exist_ok=True)
    
    # Step 1: Convert .ico to .png
    print(f"{Back.CYAN}\nStarting{Style.RESET_ALL} conversion process...\n")

    # Wait for 5 seconds
    time.sleep(5)
    
    # clear screen
    clear()

    # run convert command
    convert_ico_to_png(ico_directory, png_directory)

    # conversion waiting
    print(f"\n{Back.CYAN}Conversion completed.{Style.RESET_ALL} Waiting for 10 seconds before verifying...")
    
    # Step 2: Wait for 10 seconds
    time.sleep(10)
    
    # Step 3: Count and compare files
    print(f"\n{Fore.CYAN}Verifying conversion...\n")
    ico_count = count_files_with_extension(ico_directory, ".ico")
    png_count = count_files_with_extension(png_directory, ".png")
    
    # Display results
    print(f"{Fore.YELLOW}Total {Style.RESET_ALL}.ico files {Fore.YELLOW}in {Style.RESET_ALL}'{ico_directory}': {ico_count}")
    print(f"{Fore.YELLOW}Total {Style.RESET_ALL}.png files {Fore.YELLOW}in {Style.RESET_ALL}'{png_directory}': {png_count}")
    
    # Check if the counts match
    if ico_count == png_count:
        print(f"\n{Back.GREEN}Success{Style.RESET_ALL}: All .ico files were converted to .png files.\n")
    else:
        print(f"\n{Back.RED}Warning{Style.RESET_ALL}: Counts do not match. Some files may not have been converted.\n")
