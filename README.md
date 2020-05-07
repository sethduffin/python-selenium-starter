# Getting Started

1. Install Chrome Driver:
	1. Go to: https://sites.google.com/a/chromium.org/chromedriver/home
	2. Download chrome driver
	3. Unzip chromedriver
	4. Move file to usr/local/bin 
    ```
    cd Downloads
    mv chromedriver /usr/local/bin
    ```
2. Install Brew 
	1. Go to: https://brew.sh
3. Install Python 3 
	```
	brew install python3
	```
4. Check that Python 3 is installed
	```
	python3
	quit()
	```
5. Install Selenium
	```
	pip install selenium
	```

Execute "run" to to launch your script!

Note: On the first lauch it will ask you to verify chromedriver. To do this, go to System Preferences > Security & Privacy > General > chomedriver: Allow anyways

Refer to [Selenium with Python](https://selenium-python.readthedocs.io/) for detailed docs