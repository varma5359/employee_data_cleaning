

mkdir data
mkdir data\raw
mkdir data\processed
mkdir data\rejected
mkdir reports
mkdir src
mkdir tests
mkdir config

type nul > main.py
type nul > app.py
type nul > requirements.txt
type nul > README.md

type nul > data\raw\employees.csv
type nul > data\raw\departments.csv
type nul > data\raw\attendance.csv
type nul > data\raw\payroll.csv

type nul > src\__init__.py
type nul > src\reader.py
type nul > src\profiler.py
type nul > src\cleaner.py
type nul > src\string_cleaner.py
type nul > src\numeric_cleaner.py
type nul > src\date_cleaner.py
type nul > src\validator.py
type nul > src\transformer.py
type nul > src\exporter.py
type nul > src\pipeline.py

type nul > tests\test_reader.py
type nul > tests\test_cleaner.py
type nul > tests\test_numeric_cleaner.py
type nul > tests\test_date_cleaner.py
type nul > tests\test_validator.py

type nul > config\cleaning_rules.yaml

mkdir reports\quality
mkdir reports\summary