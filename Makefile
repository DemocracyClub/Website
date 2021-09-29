.PHONY: all
all: clean lambda-layers/DependenciesLayer/requirements.txt

.PHONY: clean
clean: ## Delete any generated static asset or req.txt files and git-restore the rendered API documentation file
	rm -rf lambda-layers/DependenciesLayer/requirements.txt

lambda-layers/DependenciesLayer/requirements.txt:
	pipenv lock -r | sed "s/^-e //" >lambda-layers/DependenciesLayer/requirements.txt


