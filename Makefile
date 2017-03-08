OK_COLOR=\033[32;01m
NO_COLOR=\033[0m

all: test

export PYTHONPATH:=${PWD}
version=`python -c 'import grappa_http; print(grappa_http.__version__)'`
filename=grappa-http-`python -c 'import grappa_http; print(grappa_http.__version__)'`.tar.gz

apidocs:
	@sphinx-apidoc -f --follow-links -H "API documentation" -o docs/source grappa_http

htmldocs:
	@rm -rf docs/_build
	$(MAKE) -C docs html

lint:
	@printf "$(OK_COLOR)==> Linting code...$(NO_COLOR)\n"
	@flake8 .

test: lint
	@printf "$(OK_COLOR)==> Runnings tests...$(NO_COLOR)\n"
	@pytest -s -v --tb=native --capture=sys --cov grappa_http --cov-report term-missing

coverage:
	@coverage run --source grappa_http -m py.test
	@coverage report

bump:
	@bumpversion --current-version $(version) patch grappa_http/__init__.py

history:
	@git changelog --tag $(version)

tag:
	@printf "$(OK_COLOR)==> Creating tag $(version)...$(NO_COLOR)\n"
	@git tag -a "v$(version)" -m "Version $(version)"
	@printf "$(OK_COLOR)==> Pushing tag $(version) to origin...$(NO_COLOR)\n"
	@git push origin "v$(version)"

clean:
	@printf "$(OK_COLOR)==> Cleaning up files that are already in .gitignore...$(NO_COLOR)\n"
	@for pattern in `cat .gitignore`; do find . -name "$$pattern" -delete; done

release: clean publish
	@printf "$(OK_COLOR)==> Exporting to $(filename)...$(NO_COLOR)\n"
	@tar czf $(filename) grappa_http setup.py README.rst LICENSE

publish:
	@echo "$(OK_COLOR)==> Releasing package $(version)...$(NO_COLOR)"
	@python setup.py register
	@python setup.py sdist upload
	@python setup.py bdist_wheel --universal upload
	@rm -fr build dist .egg grappa_http.egg-info
