install:
	bash -c "python3 -m venv env && source env/bin/activate && pip install -r requirements.txt"

start:
	bash -c "source env/bin/activate && python main.py"

ql:
	bash -c "source env/bin/activate && python ql_runner.py"

ql-test:
	bash -c "source env/bin/activate && python ql_tester.py"
