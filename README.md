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


logger.addHandeler(console_handeler)
logger.addHandeler(file_handeler)
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


# `# Project Workflow:`

<br>
<br>

**#1. Building Pipeline:**
- **1>** Create a GitHub repo and clone it in local (Add experiments).<br>
- **2>** Add src folder along with all components(run them individually).<br>
- **3>** Add data, models, reports directories to .gitignore file.<br>
- **4>** Now git add, commit, push.<br>


`Now, in our src file we have i) data_ingestion.py ii) data_preprocessing.py iii) feature_engineering.py iv) model_building.py v) model_evaluation.py But in Production Environment we need to automated all those thing. To do so we can make another .py file to connect all those thing. But it's not efficient. We will Make a Pipeline by the help of DVC.`


**#2. Setting up dcv pipeline (without params)**
- **5>** Create dvc.yaml file and add stages to it. <br>
- **6>** dvc init then do "dvc repro" to test the pipeline automation. (check dvc dag) <br>
- **7>** Now git add, commit, push <br>

`While working with ML, we have to do hyper parameter tunning or we need to change the parameter value. So, instead of going each file and change the parameter it's a very headache work. However, is there one file and we do changes in that file. So, we will create a another yaml file named params.ymal file. where we keep all the parameter.`

**#3. Setting up dcv pipeline (with params)**
- **8>** add params.yaml file <br>
- **9>** Add the params setup (mentioned below)<br>
- **10>** Do "dvc repro" again to test the pipeline along with the params<br>
- **11>** Now git add, commit, push<br>


**#4. Expermients with DVC:**
- **12>** pip install dvclive<br>
- **13>** Add the dvclive code block (mentioned below)<br>
- **14>** Do "dvc exp run", it will create a new dvc.yaml(if already not there) and dvclive directory (each run will be considered as an experiment by DVC)<br>
- **15>** Do "dvc exp show" on terminal to see the experiments or use extension on VSCode (install dvc extension)<br>
- **16>** Do "dvc exp remove {exp-name}" to remove exp (optional) | "dvc exp apply {exp-name}" to reproduce prev exp.<br>
- **17>** Change params, re-run code (produce new experiments)<br>
- **18>** Now git add, commit, push<br>

<br>

---

<br>

**#1. params.yaml setup:**
- **1>** import yaml
- **2>** add func:
```python 
def load_params(params_path: str) -> dict:
    """Load parameters from a YAML file."""
    try:
        with open(params_path, 'r') as file:
            params = yaml.safe_load(file)
        logger.debug('Parameters retrieved from %s', params_path)
        return params
    except FileNotFoundError:
        logger.error('File not found: %s', params_path)
        raise
    except yaml.YAMLError as e:
        logger.error('YAML error: %s', e)
        raise
    except Exception as e:
        logger.error('Unexpected error: %s', e)
        raise
```

- **3>** Add to main():

**#2. data_ingestion:**
```python 
params = load_params(params_path='params.yaml')
test_size = params['data_ingestion']['test_size']
```

**#3. feature_engineering:**
```python
params = load_params(params_path='params.yaml')
max_features = params['feature_engineering']['max_features']
```
**#4. model_building:**
```python
params = load_params('params.yaml')['model_building']
```

---
---

**#1. dvclive code block:**

- **1>** import dvclive and yaml:
```python
from dvclive import Live
import yaml
```
- **2>** Add the load_params function and initiate "params" var in main <br>

- **3>** Add below code block to main: <br>

```python
with Live(save_dvc_exp=True) as live:
    live.log_metric('accuracy', accuracy_score(y_test, y_test))
    live.log_metric('precision', precision_score(y_test, y_test))
    live.log_metric('recall', recall_score(y_test, y_test))
    live.log_params(params)
```
