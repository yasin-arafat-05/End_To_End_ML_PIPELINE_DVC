<br>

# `#01 End_To_End_ML_PIPELINE_DVC_AWS:`

<br>

### `Agenda:`

- 1. Create an end to end ML pipeline. **(Logging, Exception etc)**
- 2. Automate the pipeline using DVC. **(YAML crash course)**
- 3. Adding configurable params to pipeline.
- 4. Experiment tracking using dvclive.
- 5. AWS setup with DVC for data versioning.

### `ML PIPELINE FLOWS:`

Data Ingestion -> Pre-processing -> Feature Engg. -> Model Training -> Model Evalution

## `ML Flow:`

- 1. Create a Expriments folder. In, the folder do the 1st expriment in .ipynb file.

- 2. Create  a src folder, make data_ingestion.py file.`In this file we will fetch the data from a github. But in future we will fetch data from database of AWS S3 bucket.`

<br>
<br>

# `#01 Logging Module in Python:`

<br>
<br>

```python

import logging

logger = logging.getLogger("data_injection")
logger.setLevel("DEBUG")
formater = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

console_handeler = logging.StreamHandler()
console_handeler.setLevel("DEBUG")
console_handeler.setFormatter(formater)

file_handeler = logging.FileHandler()
file_handeler.setLevel("DEBUG")
file_handeler.setFormatter(formater)

```

In python logging module, we create a object of logging.getLogger("data_injection") where the object name is logger. Where, we specify the name of that looging.getLogger() object. After that, logger.setLevel("DUBUG").

Mainly, we use **logging.StreamHandler()** and **logging.FileHandler()**. Logging module is used manage the log. **StreamHandler()** is used to show the log in the terminal and **FileHandler()** is used to save the log into a file. 

**What is formater?**
By using logging.Formatter() we format how we show the output. we pass all the formater to our console_handeler or file_handeler.

**What is setLevel()?**
When we do code, everthing is working or not to ensure that we do debug. There also be warnning etc. In production level we will also get error. In, setLevel() we define the which kind of error we want to get with our logging function. Level can be define by, 
- DEBUG
- INFO
- WARNNING
- ERROR
- CRITICAL
If we set DEBUG then our logging will catch INFO,WARNNING,ERROR and CRITICAL Error.

<br>
<br>




