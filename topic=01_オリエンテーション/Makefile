QMD := $(wildcard *.qmd)
HTML := $(QMD:.qmd=.html)

.PHONY: render pdf clean

render: $(HTML)

%.html: %.qmd
	quarto render "$<"

pdf: $(HTML)
	npx decktape reveal --chrome-arg=--no-sandbox "$(HTML)" "$(HTML:.html=.pdf)"

clean:
	rm -f $(HTML) $(HTML:.html=.pdf)
