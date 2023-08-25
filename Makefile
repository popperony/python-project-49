
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

.PHONY: brain-even
brain-even:
	poetry run brain-even

.PHONY: brain-calc
brain-calc:
	poetry run brain-calc

lint:
	poetry run flake8 brain_games
