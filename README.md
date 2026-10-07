# 📄 Resume Validator Service

A **Django REST API** that validates resume fields against a configurable property schema.

Given a field name and value, the service checks whether the value meets the defined rules for that field and returns a validation result. ✅

## 🛠️ Stack

| Layer        | Technology                    |
| ------------ | ----------------------------- |
| 🚀 Framework | Django, Django REST Framework |
| 🐍 Language  | Python                        |
| 🗄️ Storage  | SQLite                        |

## ⚙️ Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/SaiHariB/Resume-Validation-Service.git
```

### 2️⃣ Navigate to the Project

```bash
cd Resume-Validation-Service
```

### 3️⃣ Create a Virtual Environment

```bash
python -m venv .venv
```

### 4️⃣ Activate the Virtual Environment

**🪟 Windows**

```bash
.venv\Scripts\activate
```

**🐧 Linux / macOS**

```bash
source .venv/bin/activate
```

### 5️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 6️⃣ Run Database Migrations

```bash
python manage.py migrate
```

### 7️⃣ Start the Development Server

```bash
python manage.py runserver
```

🌐 The application will be available at:

```text
http://127.0.0.1:8000/
```

## 🔌 API Usage

### 📝 Validate a Resume Field

```text
GET /index/?q=<field_name>&d=<value>
```

### 💡 Example

```bash
curl "http://localhost:8000/index/?q=Name&d=Rakesh"
```

### 📤 Response

```json
{
  "field": "Name",
  "value": "Sai Hari",
  "valid": true
}
```

## ⚙️ Configuration

Validation rules are defined in:

```text
validator/resume_properties.json
```

You can **add or modify field validation rules** in this file without changing the application code. 🔧

This makes the validation system **configurable, flexible, and easy to extend**. 🚀

## 📂 Project Structure

```text
Resume-Validation-Service/
│
├── 📁 resumevalidator/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── 📁 validator/
│   ├── views.py
│   ├── urls.py
│   ├── models.py
│   ├── puzzle_resolver.py
│   └── resume_properties.json
│
├── 📄 manage.py
├── 📄 requirements.txt
└── 📄 README.md
```

## ✨ Features

* 📄 Resume field validation
* ⚙️ Configurable validation rules
* 🔌 Django REST API
* 🗂️ JSON-based property configuration
* 🗄️ SQLite database support
* 🔧 Easy to extend with additional resume fields
* 🚀 Simple and lightweight backend service

## 🎯 Future Enhancements

* 📑 PDF and DOCX resume parsing
* 🤖 AI-based resume analysis
* 🎯 Job description matching
* 📊 Resume scoring system
* 🔍 Automated skill extraction
* 🏆 Candidate ranking

