Selenium, Pytest, Logging, HTML Reports
Create virtual environment:
 'python - venv .\venv'
 This will create virtual environment 'venv' directory in location C:\automation\sitestautomationpython

-Activate the virtual environment:
 .\venv\Scripts\activate

-Install all the python packages needed for automation framework:
 pip install -r requirements.txt

Modification of pytest.ini
	testpaths = tests/web
	specify the value for 'testpaths' if you want pytest to search and pick tests any other desired location,
	Default value is tests/web
