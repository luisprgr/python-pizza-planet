build-AppLayer:
	mkdir -p "$(ARTIFACTS_DIR)/python"
	mkdir -p "$(ARTIFACTS_DIR)/python/app"
	cp -r "common/" "$(ARTIFACTS_DIR)/python/app/"
	cp -r "controllers/" "$(ARTIFACTS_DIR)/python/app/"
	cp -r "repositories/" "$(ARTIFACTS_DIR)/python/app/"
	cp -r "services/" "$(ARTIFACTS_DIR)/python/app/"
	cp __init__.py "$(ARTIFACTS_DIR)/python/app/"
	cp plugins.py "$(ARTIFACTS_DIR)/python/app/"
	cp settings.py "$(ARTIFACTS_DIR)/python/app/"
	python -m pip install -r requirements.txt -t "$(ARTIFACTS_DIR)/python"
