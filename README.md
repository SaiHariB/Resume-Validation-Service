ResumeValidatorService
A Django REST API that validates resume fields against a configurable property schema. Given a field name and value, it checks whether the value meets the defined rules for that field and returns a validation result.

Stack
Layer	Technology
Framework	Django, Django REST Framework
Language	Python
Storage	SQLite
Setup
git clone https://github.com/RakeshGanapathy/ResumeValidatorService.git
cd ResumeValidatorService
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
API Usage
# Validate a resume field
GET /index/?q=<field_name>&d=<value>

# Example
curl "http://localhost:8000/index/?q=Name&d=Rakesh"
Response:

{
  "field": "Name",
  "value": "Rakesh",
  "valid": true
}
Configuration
Validation rules are defined in resume_properties.json. Add or modify field rules there without changing application code.
