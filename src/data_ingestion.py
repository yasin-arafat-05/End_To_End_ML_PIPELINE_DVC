import os 
import logging
import pandas as pd 
from sklearn.model_selection import train_test_split


# directory where our log file will be saved:
dirs = "logs"
os.makedirs(dirs,exist_ok=True)


# logger configuration:
logger = logging.getLogger("data_injection")
logger.setLevel("DEBUG")
formater = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')


# StreamHandler for showing the log in the terminal
console_handeler = logging.StreamHandler()
console_handeler.setLevel("DEBUG")
console_handeler.setFormatter(formater)


# FileHandler for save the log into file
log_file_path = os.path.join(dirs,"data_ingestion.txt")
file_handeler = logging.FileHandler(log_file_path)
file_handeler.setLevel("DEBUG")
file_handeler.setFormatter(formater)

# add logger:
logger.addHandler(console_handeler)
logger.addHandler(file_handeler)



# =========== Load the dataset ===========
def load_data(data_url:str) -> pd.DataFrame:
    try: 
        df = pd.read_csv(data_url,sep=",")
        logger.debug(msg="Data Loaded from: {}".format(data_url))
        return df 
    except pd.errors.ParserError as e:
        logger.error(f"Failed to parse csv at {data_url} {e}")
        raise
    except Exception as e:
        logger.error(f"Unexpected error while loding the data {data_url} {e}")
        raise
    
    

# ============== preprocess the data =============
def process_data(df:pd.DataFrame)->pd.DataFrame:
    try:
        print(f"{df.columns}")
        df.drop(columns = ['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], inplace = True)
        df.rename(columns={"v1":"target","v2":"text"},inplace=True)
        logger.debug("basic data preprocessing is complete")
        return df
    except KeyError as e:
        logger.error("Missing Column in the dataset {}".format(e))
        raise
    except Exception as e:
        logger.error("Unexpected error during basic preprocessing {}".format(e))
        raise
    

# ================== save the data ==================
def save_data(train:pd.DataFrame,test:pd.DataFrame,data_path:str)->None:
    try: 
        raw_data_path =  os.path.join(data_path,"raw")
        os.makedirs(raw_data_path,exist_ok=True)
        train.to_csv(os.path.join(raw_data_path,"train.csv"),index=False)
        test.to_csv(os.path.join(raw_data_path,"test.csv"),index=False)
        logger.debug(f"Train and test data save {raw_data_path}")
    except Exception as e:
        logger.error(f"Unexpected error while saving the data at  {data_path} error {e}")
        raise
    



def main():
    try: 
        test_size = 0.2 
        # we are taking it from github but later we will take it from aws or other resources
        data_url ="https://raw.githubusercontent.com/yasin-arafat-05/End_To_End_ML_PIPELINE_DVC/refs/heads/main/expriments/spam.csv"
        df = load_data(data_url=data_url)
        final_df = process_data(df)
        train_data,test_data = train_test_split(final_df,test_size=test_size,random_state=2)
        save_data(train_data,test_data,data_path="./data")
    except Exception as e:
        logger.error(f"Faied to comlete the data ingestion process. {e}")
        
    
    
    
if __name__ == "__main__":
    main()
    
    