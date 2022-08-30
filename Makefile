URL="https://magic.wizards.com/ja/articles/archive/card-image-gallery/dominaria-united"

run:
	python main.py

download:
	curl $(URL) > index.html

shell:
	poetry shell

