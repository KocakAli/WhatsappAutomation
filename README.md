# WhatsappAutomation
Script automatically sends messages via WhatsApp Web without saved contacts using the contact data and message data in the excel sheet when it is run.If a problem occurs or script does not run properly just contact me.

### Requirements and Install


#### Python
<img src="https://www.python.org/static/img/python-logo.png" width="124">

You need to install python if you have not install it yet. Visit [python offical web page](https://www.python.org/downloads/) to install python. You can choose a python version which is compatible with your operating system from this page.


#### Packages
You must install the packages in the requirements.txt file to run script. You can install the required packages one by one 

- ***pip install pandas***
- ***pip install xlrd***
- ***pip install selenium***
- ***pip install webdriver_manager***
- ***pip install openpyxl***

or just use in your terminal.        
- ***pip install -r requirements.txt***

#### Chromedriver
You dont have to download chromedriver because we use webdrive_manager package for start a chrome browser.



### Usage 
You need an excel worksheet with two columns named ***contact*** and ***message*** in the same directory with your script.py file. Write the people you want to send message in contact column and write message that you want send in message column.

<img src="https://user-images.githubusercontent.com/68864416/190374045-a46ce959-2c5b-47cc-be73-63bcaa1141fb.PNG" width="600"> <img src="https://user-images.githubusercontent.com/68864416/190372569-126cb407-c192-4103-8b40-f1ba988f6793.png" width="360">

#### Run script
After create an excel workbook open your terminal and run ```python script.py```. This will start automatically a chrome browser. After logged in with QR code press the enter on terminal. Message will send to contacts.
![doc1](https://user-images.githubusercontent.com/68864416/190375585-ef61251d-9afa-46dc-84b4-f2aa3cfa140a.PNG)
![doc3](https://user-images.githubusercontent.com/68864416/190375831-831f559a-7b85-49aa-b303-a8307bc2a619.PNG)
<div>
  <img src="https://user-images.githubusercontent.com/68864416/190376035-4a04a778-5065-45c5-a636-f786c92af594.PNG" width="720">
<div>




### Author Note
This script is for educational purposes. Commercial use of this repo is strictly prohibited.
It is not affiliated with whatsapp and its subsidiaries, it is completely independent and unoffical software. Use at your own risk. 
