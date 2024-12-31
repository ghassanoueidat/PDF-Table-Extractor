
#!/bin/bash

echo "🚀 Starting the PDF-Table-Extractor Setup Process on macOS/Linux..."

# Step 1: Create a virtual environment
echo "🛠️ Creating a virtual environment..."
python3 -m venv venv

# Step 2: Activate the virtual environment
echo "✅ Activating the virtual environment..."
source venv/bin/activate

# Step 3: Install dependencies
echo "📦 Installing dependencies from requirements.txt..."
pip install -r requirements.txt

# Step 4: Verify installations
echo "🔍 Verifying installations..."
python3 --version
gs --version

echo "🎯 Setup completed successfully!"
echo "💡 Next Steps:"
echo "1. Activate the virtual environment: source venv/bin/activate"
echo "2. Run the script: python pdf_table_extractor.py"
