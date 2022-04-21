# visicom

This repository contains python wrapper around visicom's geocoding endpoint.


## Installation:
```
$ git clone https://github.com/hp0404/visicompy.git
$ cd visicompy
$ python -m venv env 
$ . env/Scripts/activate
$ pip install -r requirements.txt
$ python setup.py develop
```

## Usage
```python
>>> from visicom import Visicom
>>> api = Visicom(token="414eb149c5b857fb898dbaf80bcb1def")
>>> api.geocode(address="м. Київ, вул. Хрещатик, 26")
[30.521626, 50.448847]
>>> api.geocode(address="м. Київ, вул. Полярна, 5")
[30.453879, 50.521189]
```