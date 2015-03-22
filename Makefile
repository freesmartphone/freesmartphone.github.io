MKDOCS=mkdocs

all: build

build: .stamp-build

.stamp-build:
	rm -rf site
	$(MKDOCS) build
	touch $@

deploy: build
	git add site -m"update docs"
	git subtree push --prefix site origin master

clean:
	rm -rf .stamp*
