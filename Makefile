install:
	@echo "Installing ..."
	@./install.sh

step:
	@echo "Committing a step to Github ..."
	git add .
	git commit -m "step"
	git push

release:
	@echo "Releasing ..."
	@./release.sh

test:
	@echo "Launching tests ..."
	@./run_tests.sh
