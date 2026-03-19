DIRS := $(wildcard topic=*/)
SRCS := $(foreach d,$(DIRS),$(wildcard $(d)$(notdir $(d:/=)).qmd))
HTMLS := $(SRCS:.qmd=.html)
PDFS := $(SRCS:.qmd=.pdf)

.PHONY: all html pdf clean

all: html pdf

html: $(HTMLS)

pdf: $(PDFS)

%.html: %.qmd
	quarto render "$<"

%.pdf: %.html
	cd "$(dir $<)" && npx decktape reveal --chrome-arg=--no-sandbox "$(notdir $<)" "$(notdir $@)"

clean:
	rm -f $(HTMLS) $(PDFS)