.PHONY: format

format:
	black .
	isort --profile black .
	astyle --indent=spaces=4 --style=allman --indent-labels --indent-preprocessor --indent-col1-comments \
		--max-instatement-indent=60 --min-conditional-indent=0 --pad-oper --unpad-paren --pad-paren-in \
		--break-closing-brackets --add-brackets --keep-one-line-blocks --keep-one-line-statements \
		--convert-tabs --align-pointer=name --align-reference=name --suffix=none --options=none \
		--recursive *.cpp *.h
