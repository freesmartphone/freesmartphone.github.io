## freesmartphone.org top-level documentation

This project is using [mkdocs](http://www.mkdocs.org).

Note that the ```devel``` branch contains the actual source and the ```master``` branch should only contain the ```site``` subdirectory.

If you want to commit an update, please only change the md files (*not* the HTML files) and then call the following sequence of commands:

```mkdocs build``` – this will rebuild the html files

```git commit -a -m"your message"``` – this will commit your changes

```git push``` – this will push the changes to ```devel```

```git subtree push --prefix site origin master``` – this will push the site subdirectory to master and triggers github to rebuild our site documentation at [www.freesmartphone.org](http://www.freesmartphone.org)

