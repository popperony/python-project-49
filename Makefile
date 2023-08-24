
.PHONY: install
install:
	poetry install

.PHONY: build
build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

.PHONY: brain-games
brain-games:
	poetry run brain-games

lint:
	poetry run flake8 brain_games
