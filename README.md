# Yolov8 Personal Guide

## 💻 Installation (MacOS/Window)

### Note: How to install on the desired python version

- `python` can be specified by `py`, `python3` or `python_version_`. For example, `python3.11.6`
- The same thing to `pip` `pip(_python_version_)`. For example, `pip3.11.6`, which will install on the according version of python
- At the time this is writen, Nov 22 2023, ultralytics DOES NOT work with python 3.12, so I have to use a lower version.

Check if python installed: 
```
python --version
```
### 1. Install `pip`

```
python(desire_python_version) get-pip.py
```
Example: `python3.11.6 get-pip.py`
Check if pip installed:
```
pip -V
```

### 2. Install ultralytics

```
pip(desire_python_version) install ultralytics
```
Example: `pip3.11.6 install ultralytics`

### 3.Import to python

To open the desired python version. Run:
```
python3.11.6
```
Then:
```
>>> import ultralytics
```

### 4. Good to go!
Go to VS code and `control` `shift` `p` to find `select python interpreter` and pick the desire version.

## 📅 Import dataset

- Note: The common problem is ultralytics cannot find the path to the dataset.
- Goals: the idea is to make `C:\Users\PC\AppData\Roaming\Ultralytics\settings.yaml` file point to the correct project path.
- This means that if I don't want the dataset to be exposed, I can just put it in a local folder and have `settings.yaml` point to it rather than put the dataset into the project. 


### 1. Reset ultralytics settings

Go to the **PARENT FOLDER** of the datasets, Run the following `reset_settings.py`. 
```
from ultralytics import settings
settings.reset()
```
Which allows ultralytics setting file to point to the current project.

### 2. Rename the dataset

The dataset folder must be `datasets`. 
Since the `settings.yaml` is now pointing to `SomePath/PARENT_FOLDER/datasets`

### 3. Locate the `.yaml` file and run the script

The `data.yaml` is a relative path. Example: `folderName/something.yaml`
```
from ultralytics import YOLO

# Load a model
model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)

# Train the model
model.train(data="data.yaml", epochs=7)  # train the model
metrics = model.val()  # evaluate model performance on the validation set
path = model.export(format="onnx")  # export the model to ONNX format

```




## ✅ Project completion checklist

### 1. requirement.txt
To generate one, run:
```
pip3 freeze > requirements.txt 
```

## 💽 Import other project's model

1. Import `best.pt` and `requirement.txt`
2. Install dependencies from `requirement.txt`
   ```
   # I HAVE NOT TRIED THIS YET
   pip install -r /path/to/requirements.txt
   ```
