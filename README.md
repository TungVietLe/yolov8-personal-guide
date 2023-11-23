# yolov8-personal-guide

## installation (MacOS/Window)

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

## Import dataset

Note: The common problem is ultralytics cannot find the path to the dataset.

### 1. Reset ultralytics settings

Run the following `reset_settings.py` in the PATH OF THE DESIRE PROJECT. 
```
from ultralytics import settings
settings.reset()
```
Which allows ultralytics setting file to point to the current project.

### 2. Rename the dataset

The dataset folder must be `datasets`. 

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
