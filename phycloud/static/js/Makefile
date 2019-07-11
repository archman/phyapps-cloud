all:
	for i in $(shell ls *.js); \
	do \
		minify $$i -o $${i%%.js}.min.js; \
	done
