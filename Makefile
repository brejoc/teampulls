all: black

black:
	black --line-length 90 src/teampulls

.PHONY: black
