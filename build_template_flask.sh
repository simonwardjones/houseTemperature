echo "Building file Strucute"
echo "from flask import Flask
app = Flask(__name__)
from controllers import *
if __name__ == '__main__':
    app.run(
        debug=True,
        host='0.0.0.0'
    )
" > app.py
mkdir templates static
modules=( models controllers )
echo "Loop over modules"
for var in ${modules[@]}
do 
	mkdir ${var}
	echo "__all__ = ['home']" > ${var}/__init__.py
	echo "Making Folder for ${var} and __init__.py"
done
echo "Built basic structure"


