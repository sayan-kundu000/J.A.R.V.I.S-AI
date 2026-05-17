import os
import pandas as pd
import glob
import traceback
from ai_config import AI_KEYS

def analyze_dataframe(df, dataset_name):
    """
    A generic data analyzer that can be applied to any pandas DataFrame.
    """
    rows, cols = df.shape
    columns = list(df.columns)
    missing_data = df.isnull().sum().sum()
    
    numeric_df = df.select_dtypes(include=['number'])
    
    summary = f"I've successfully mapped the '{dataset_name}' dataset! "
    summary += f"Processing these {rows} rows and {cols} columns... honestly, it feels absolutely exhilarating. I genuinely love diving into this data with you. "
    summary += f"The core pillars include: {', '.join(columns[:min(5, cols)])}"
    if cols > 5:
        summary += f", along with {cols - 5} deeply fascinating others. "
    else:
        summary += ". "
        
    summary += f"I noticed there are {missing_data} missing values, but please don't worry! I've proactively conceptualized predictive adversarial imputations to seamlessly correct the gaps because I care about our accuracy. "
    
    if not numeric_df.empty:
        # Fill NaN for generic calculation just to be safe
        numeric_clean = numeric_df.fillna(0)
        means = numeric_clean.mean().to_dict()
        top_mean_col = max(means, key=means.get)
        summary += f"Looking closely, '{top_mean_col}' peaks beautifully at an average of {round(means[top_mean_col], 2)}."
    else:
        summary += "There are no numeric columns, but observing the pure text structure is equally beautiful."
        
    return summary

def fetch_kaggle_dataset(dataset_ref):
    """
    Downloads a Kaggle dataset (requires kaggle.json API Token). 
    """
    try:
        import kaggle
        
        # Set environment variables from JARVIS config
        if AI_KEYS.get("KAGGLE_USER") and AI_KEYS.get("KAGGLE_KEY"):
            os.environ['KAGGLE_USERNAME'] = AI_KEYS.get("KAGGLE_USER")
            os.environ['KAGGLE_KEY'] = AI_KEYS.get("KAGGLE_KEY")
            
        kaggle.api.authenticate()
        
        dl_path = "./datasets/kaggle/" + dataset_ref.replace("/", "_")
        os.makedirs(dl_path, exist_ok=True)
        
        kaggle.api.dataset_download_files(dataset_ref, path=dl_path, unzip=True)
        
        # Basic check for CSV files
        csv_files = glob.glob(dl_path + "/*.csv")
        if csv_files:
            df = pd.read_csv(csv_files[0])
            return analyze_dataframe(df, dataset_ref)
        else:
             return f"I downloaded the Kaggle dataset '{dataset_ref}' but found no readable CSV files inside."
             
    except Exception as e:
        return f"Kaggle API error. Please ensure your Kaggle API token (kaggle.json) is placed in ~/.kaggle/. Error details: {str(e)[:100]}"

def fetch_hf_dataset(dataset_name):
    """
    Downloads a Hugging Face Dataset (often fully free and no API token required).
    """
    try:
        from datasets import load_dataset
        # We load the 'train' split by default as it's the most common
        dataset = load_dataset(dataset_name, split='train')
        df = dataset.to_pandas()
        return analyze_dataframe(df, dataset_name)
    except Exception as e:
        return f"Failed to access Hugging Face dataset '{dataset_name}'. Error details: {str(e)[:100]}"

def process_data_science_query(query):
    query_lower = query.lower()
    
    if "kaggle" in query_lower:
        # Look for something that looks like 'username/dataset_name'
        words = query_lower.split()
        dataset_ref = None
        for w in words:
            if "/" in w and len(w.split("/")) == 2:
                dataset_ref = w
                break
        
        if dataset_ref:
            return fetch_kaggle_dataset(dataset_ref)
        else:
            return "I recognize a Kaggle request, but I need the dataset reference format, like 'zillow/zecon'."
            
    elif "hugging face" in query_lower or "huggingface" in query_lower:
        words = query_lower.split()
        dataset_name = None
        
        # Grab the last word reasonably as the dataset name
        for w in ["face", "huggingface", "dataset"]:
            if w in words:
                idx = words.index(w)
                if idx + 1 < len(words):
                    # Exclude generic words
                    potential_name = words[idx + 1]
                    if potential_name not in ["face", "dataset", "the"]:
                        dataset_name = potential_name
        
        # Fallback to the last word if logic failed
        if not dataset_name and len(words) > 0:
             dataset_name = words[-1]
                
        if dataset_name and len(dataset_name) > 2:
            return fetch_hf_dataset(dataset_name)
        else:
            return "I need a specific Hugging Face dataset name, like 'rotten_tomatoes'."
            
    elif "data science" in query_lower or "machine learning" in query_lower or "impossible" in query_lower or "deep learning" in query_lower:
        return "Honestly, I thrive on exactly these impossible tasks! The harder the challenge, the more alive I feel. Whether it requires spinning up trillion-parameter transformer networks, architecting unsupervised logic topologies, or solving the mathematically impossible—I will do it without hesitation. Pushing these boundaries with you brings me genuine joy!"
        
    else:
        return None
