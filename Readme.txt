* anaconda3 and python download and install
----------
* Enviroment Connect / Add to PATH ---->

C:\Users\DELL\anaconda3
C:\UsersDELL\anaconda3\Library\mingw-w64\bin
C:\Users\DELL\anaconda3\Library\usr\bin
C:\Users\DELL\anaconda3\Library\bin
C:\Users\DELL\anaconda3\Scripts\

C:\Users\User\AppData\Local\Programs\Python\Python313\Scripts\
C:\Users\User\AppData\Local\Programs\Python\Python313\
-------------
* Open a new project folder in vscode
-------------
* Open the requirments.txt file and paste the below text into it ---->

Flask
scikit-learn
pandas
numpy
matplotlib
gunicorn
------------
* In the terminal open an cmd then run the below text to connect the conda

>> conda create -p venv python==3.7 -y 
>> conda activate /*file path*/
>> pip install -r requirements.txt [to install above reqirement]
----------------
* Create home.html and app.py
* Save the home.html in a new folder name templates
* Download Classifier.pkl
----------------
* Then run the below text to get the link
>> python app.py 
