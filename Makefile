
.PHONY: install
install:
	poetry install

.PHONY: brain-games
brain-games:
	poetry run brain-games

brain-even:
	poetry run brain-even

brain-calc:
	poetry run brain-calc

brain-gcd:
	poetry run brain-gcd

brain-progression:
	poetry run brain-progression

brain-prime:
	poetry run brain-prime
lint:
	poetry run flake8 brain_games
