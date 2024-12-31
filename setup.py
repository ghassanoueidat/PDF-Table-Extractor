
# setup.py

import os
import subprocess
import sys

def run_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        sys.exit(1)

def main():
    print("🚀 Starting the PDF-Table-Extractor Setup Process...
")
    
    # Step 1: Create a virtual environment
    print("🛠️ Creating a virtual environment...")
    run_command("python -m venv venv")
    
    # Step 2: Activate the virtual environment
    if os.name == 'nt':
        activate_command = ".\venv\Scripts\activate"
    else:
        activate_command = "source venv/bin/activate"
    print("✅ Virtual environment created. Please activate it manually if needed.")
    
    # Step 3: Install dependencies
    print("📦 Installing dependencies from requirements.txt...")
    run_command(f"{activate_command} && pip install -r requirements.txt")
    
    # Step 4: Verify installations
    print("🔍 Verifying installations...")
    run_command(f"{activate_command} && python --version")
    run_command("gs --version")
    
    print("🎯 Setup completed successfully!")
    print("💡 Next Steps:")
    print("1. Activate the virtual environment:")
    if os.name == 'nt':
        print("   .\venv\Scripts\activate")
    else:
        print("   source venv/bin/activate")
    print("2. Run the script: python pdf_table_extractor.py")

if __name__ == '__main__':
    main()
