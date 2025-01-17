create-venv:
	python3 -m venv venv	

install-requirements:
	. venv/bin/activate && pip install -r requirements.txt

start-database:
	. venv/bin/activate && python3 manage.py db init
	. venv/bin/activate && python3 manage.py db migrate
	. venv/bin/activate && python3 manage.py db upgrade

delete-database:
	rm -r migrations
	rm -r pizza.sqlite

seed-database:
	. venv/bin/activate && python3 manage.py seeder

start-server:
	. venv/bin/activate && python3 manage.py run

start-hot-reload:
	. venv/bin/activate && python3 manage.py hot-reload

run-tests:
	. venv/bin/activate && pytest -v app/test/

test-coverage-report:
	. venv/bin/activate && pytest --cov-config=.coveragerc --cov=app app/test/ 

run-linters:
	. venv/bin/activate && flake8 app/ manage.py seeder.py

format-code:
	. venv/bin/activate && black app/ manage.py seeder.py --skip-string-normalization --line-length 79
