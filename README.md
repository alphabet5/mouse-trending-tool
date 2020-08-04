# mouse-trending-tool
 Tool to create a csv file of trend data using your mouse.


## Requirements
- matplotlib < 3.3.0 (https://github.com/pyinstaller/pyinstaller/issues/5004)
- python3.8.5
- pyinstaller (to create an executable)

## Build

pyinstaller --onefile --noconsole --icon=mouse-trending-tool.ico --hidden-import=pkg_resources.py2_warn mouse-trending-tool.py


## Exe Location

You can find an exe built with the above command in the dist folder.