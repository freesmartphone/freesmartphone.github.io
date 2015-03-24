MKDOCS=mkdocs

all: build

build: .stamp-build

.stamp-build:
	rm -rf site
	$(MKDOCS) build
	touch $@

deploy: build
	git stash
	git checkout master
	git add site
	git commit -m"update docs"
	git subtree push --prefix site origin master
	git checkout devel
	git stash apply

clean:
	rm -rf .stamp*
