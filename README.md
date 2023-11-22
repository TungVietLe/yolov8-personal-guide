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
