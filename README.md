# Segmentation of Bone Marrow Mesenchymal Stem Cell (MSC) Bright-Field Phase Contrast Images

This is the repository containg code, references and scripts for the
preprocessing and analysis of images of stem cells. The goal is to detect the
nuclei of Mesenchymal Stem Cells coming from the Bone Marrow of a human patient,
in order to subsequently track their positions and trace their lineages.

Images are taken using a Bright-Field Microscopy technique known as Phase
Contrast Microscopy, often used in experiments for qualitative analysis of
biological samples. The advantage of using this type of microscopy is that it
does not depend on the use of fluorescent staining agents, hence avoiding
phototoxic effects on the sample. The analysis and segmentation of the images
though is not trivial at all.

## Setup and Use

The project uses the following software/libraries:
- Python
- bash
- ImageJ/Fiji

### Setting up environment variables

There are few environment variables that must be set before using the project:

- `DATA_SRC_FOLDER`: folder containing the original images (i.e. folder of the external drive where images are saved directly from the experiment) 
- `RAW_FOLDER`: folder where only the selected images should be imported, inside the current project
- `FOLDER_REF`: csv file containing relevant informations about the subfolders of interest, and the time interval of interest
- `FIJI_BIN`: location of the ImageJ/Fiji executable

### Setting up the folders

In order to create the correct folders, run the following

```
bash prepare_folders.sh
```

### Setting up Python

You can setup an environment by issuing the command

```
python -m venv env
```

Once you have created and activated the environment

```
source ./env/bin/activate
```

you can install the required packages

```
pip install -r requirements.txt
```

### Running Python scripts

In order to **import images** run the following

```
python import_images.py
```

Remember to activate the correct environment. In case you mess up with the images,
you can clean the `./data/raw` folder by issuing the following command

```
bash clean_data.sh
```

### Running ImageJ/Fiji macros

In order to run the **image cropping** script, just run

```
$FIJI_BIN -macro ./preproc/crop_images.ijm
```

In the case of the **nuclei tagging** script, run the following

```
$FIJI_BIN -macro ./preproc/segment_images.ijm
```

The GUI will automatically open up.

## Data

## Impressum and Contact

Shoichi Yip

E-mail: yip.2053852@studenti.uniroma1.it
