This program convert cartoons into drone arrays with given size


### Requirement
- General
  - python3
  - PIL: `pip install Pillow`
- Optional (alredy in this repo): used by `weight.py`
  - `graphycs.py`
  - `Button.py`

### How to use
- File input
  - `input/`: input cartoon images
  - `tmp/`: intermediate files
  - `output/`: the output drone array image
  - `weight/`: optional weight image to decrease the density of drones in chosen area
- Scripts
  - `img2dot.py`: convert all images in `input/` into drone array images in `output/`
    - __drone_array_min__ min number of drones
	- __drone_array_max__ max number of drones
	- __debug__ turn on debug mode to show all intermediate images
  - `weight.py`: a GUI interface to produce the weight image.
