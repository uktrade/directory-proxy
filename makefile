clean:
	-find . -type f -name "*.pyc" -delete
	-find . -type d -name "__pycache__" -delete

test_requirements:
	pip install -e .[test]

FLAKE8 := flake8 . --exclude=.venv
PYTEST := pytest . --ignore=.venv --ignore=venv --cov=. --cov-config=.coveragerc --capture=no $(pytest_args)
CODECOV := \
	if [ "$$CODECOV_REPO_TOKEN" != "" ]; then \
	   codecov --token=$$CODECOV_REPO_TOKEN ;\
	fi

test:
	$(FLAKE8) && $(PYTEST) && $(CODECOV)

publish:
	rm -rf build dist; \
	python setup.py bdist_wheel; \
	twine upload --username $$DIRECTORY_PYPI_USERNAME --password $$DIRECTORY_PYPI_PASSWORD dist/*

DJANGO_WEBSERVER := \
	python manage.py runserver 0.0.0.0:$$PORT

django_webserver:
	$(DJANGO_WEBSERVER)

DEBUG_SET_ENV_VARS := \
	export SECRET_KEY=debug; \
	export PORT=8004; \
	export DEBUG=true; \
	export SECURE_HSTS_SECONDS=0; \
	export SECURE_SSL_REDIRECT=false

TEST_SET_ENV_VARS :=\
	export IP_RESTRICTOR_RESTRICT_ADMIN=false; \
	export UPSTREAM_DOMAIN=http://0.0.0.0:8003; \
	export UPSTREAM_SIGNATURE_SECRET=debug


debug_webserver:
	$(DEBUG_SET_ENV_VARS) && $(DJANGO_WEBSERVER);

debug_shell:
	$(DEBUG_SET_ENV_VARS) && ./manage.py shell

debug_test:
	$(DEBUG_SET_ENV_VARS) && $(TEST_SET_ENV_VARS) && $(FLAKE8) && $(PYTEST)

debug_pytest:
	$(DEBUG_SET_ENV_VARS) && $(TEST_SET_ENV_VARS) && $(PYTEST)

.PHONY: clean test_requirements debug_webserver debug_test
