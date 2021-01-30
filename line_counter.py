



targetFile = "main.py"

with open(targetFile) as f:
	numberOfLines = len([l for l in f.readlines() if l.strip() and not l.strip().startswith("#")])

print(numberOfLines)





