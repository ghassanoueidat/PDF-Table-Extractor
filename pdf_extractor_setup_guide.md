
# 📚 **PDF Table Extractor Setup Guide**

This guide provides step-by-step instructions for setting up and running the **PDF Table Extractor** script on **Windows**, **Linux**, and **macOS**.

---

## 📋 **Table of Contents**
1. [Prerequisites](#prerequisites)
2. [System-Specific Installations](#system-specific-installations)
3. [Common Setup Steps](#common-setup-steps)
4. [Usage Instructions](#usage-instructions)
5. [Troubleshooting](#troubleshooting)
6. [Verification Checklist](#verification-checklist)
7. [License](#license)

---

## 🛠️ **1. Prerequisites**

Make sure you have:
- **Python 3.8+**
- **Ghostscript** (Required by Camelot)
- **Poppler** (Required for Linux/macOS users)
- **PyPDF2 (Version 1.26.0)**

---

## 💻 **2. System-Specific Installations**

### **Python Installation**
- **Windows:** Download Python from [python.org](https://www.python.org/downloads/) and ensure **"Add Python to PATH"** is checked.
- **Linux:** Install Python via terminal:
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip python3-venv
   ```
- **macOS:** Install Python via Homebrew:
   ```bash
   brew install python
   ```

Verify Installation:
```bash
python --version
```

### **Ghostscript Installation**
- **Windows:** Download and install from [Ghostscript Official Site](https://www.ghostscript.com/download/gsdnld.html).
   - Add the following paths to **System PATH**:
     ```
     C:\Program Files\gs\gs10.04.0\bin
     C:\Program Files\gs\gs10.04.0\lib
     ```
- **Linux:** Install via terminal:
   ```bash
   sudo apt install ghostscript
   ```
- **macOS:** Install via Homebrew:
   ```bash
   brew install ghostscript
   ```

Verify Installation:
```bash
gs --version
```

### **Poppler Installation (Linux/macOS only)**
- **Linux:** Install via terminal:
   ```bash
   sudo apt install poppler-utils
   ```
- **macOS:** Install via Homebrew:
   ```bash
   brew install poppler
   ```

Verify Installation:
```bash
pdftoppm -h
```

---

## 🛠️ **3. Common Setup Steps**

### Step 1: Create a Virtual Environment
```bash
python -m venv venv
# Windows:
.env\Scriptsctivate
# Linux/macOS:
source venv/bin/activate
```

### Step 2: Install Required Libraries
```bash
pip install tkinter
pip install camelot-py[cv]
pip install pandas
pip install openpyxl
pip install matplotlib
pip install PyPDF2==1.26.0
```

> ⚠️ **Important:** Use **PyPDF2 version 1.26.0** for better compatibility with Camelot. Newer versions may cause parsing issues.

### Step 3: Clone the Repository
```bash
git clone https://github.com/your-username/pdf-table-extractor.git
cd pdf-table-extractor
```

### Step 4: Activate Virtual Environment
```bash
# Windows:
.env\Scriptsctivate
# Linux/macOS:
source venv/bin/activate
```

### Step 5: Run the Script
```bash
python pdf_table_extractor.py
```

---

## 🚀 **4. Usage Instructions**

1. Run the script:
   ```bash
   python pdf_table_extractor.py
   ```
2. Select a **PDF File** when prompted.
3. Wait for the tables to be extracted.
4. Choose a location to save the **JSON output**.
5. CSV files will be saved automatically for each table extracted.

---

## 🐞 **5. Troubleshooting**

### **Error 1:** `Ghostscript not found`
- Ensure Ghostscript is installed and added to `PATH`.

### **Error 2:** `ModuleNotFoundError: No module named 'camelot'`
- Ensure dependencies are installed using:
   ```bash
   pip install -r requirements.txt
   ```

### **Error 3:** `Tkinter not found`
- On Linux:
   ```bash
   sudo apt install python3-tk
   ```
- On macOS:
   ```bash
   brew install python-tk
   ```

### **Error 4:** `No tables found in the PDF`
- Ensure the PDF contains well-defined tables.
- Try switching between `lattice` and `stream` extraction flavors.

---

## ✅ **6. Verification Checklist**

- [ ] Python 3.8+ installed
- [ ] Ghostscript installed and verified
- [ ] Poppler installed (Linux/macOS)
- [ ] Required Python libraries installed
- [ ] PyPDF2 version 1.26.0 installed
- [ ] Script executes without errors

---

## 📄 **7. License**
This project is licensed under the **MIT License**.

---

If you encounter any issues, feel free to open an issue on the [GitHub repository](https://github.com/your-username/pdf-table-extractor/issues). 😊
