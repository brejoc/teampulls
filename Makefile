all: black

black:
	black --line-length 90 src/teampulls

black-check:
	black --check --line-length 90 src/teampulls

.PHONY: black black-check
