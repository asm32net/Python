@set ProjectName=PaStarry2016TK

@set _cmd1=python -O -m py_compile %ProjectName%.pyw

@echo %_cmd1%

@if exist %ProjectName%.pyw %_cmd1%

@pause