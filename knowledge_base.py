from country_brain import get_country_rankings
from finance_brain import get_top_stocks_forecast, get_gold_rates_india
import json

def get_full_knowledge_base():
    """
    Aggregates all historical and current data into a single structured object.
    """
    countries = get_country_rankings()
    stocks = get_top_stocks_forecast()
    gold = get_gold_rates_india()
    
    return {
        "countries": countries,
        "stocks": stocks,
        "gold": gold
    }

def get_historical_data():
    """
    Extracts only the historical segments of the knowledge base.
    """
    kb = get_full_knowledge_base()
    hist_data = {
        "countries": [],
        "stocks": {}, # Historical stocks not explicitly in finance_brain yet, will mock
        "gold": "Base Rate: 7450.0 INR (Historical reference)"
    }
    
    for c in kb["countries"]:
        hist_data["countries"].append({
            "country": c["country"],
            "gdp": c["gdp"]["historical"],
            "population": c["population"]["historical"],
            "aqi": c["pollution"]["historical"],
            "life_expectancy": c["life_expectancy"]["historical"],
            "education": c["education"]["historical"],
            "military": c["military"]["historical"],
            "happiness": c["happiness"]["historical"]
        })
        
    return hist_data

def get_current_data():
    """
    Extracts only the current segments of the knowledge base.
    """
    kb = get_full_knowledge_base()
    curr_data = {
        "countries": [],
        "stocks": kb["stocks"],
        "gold": kb["gold"]
    }
    
    for c in kb["countries"]:
        curr_data["countries"].append({
            "country": c["country"],
            "gdp": c["gdp"]["current"],
            "population": c["population"]["current"],
            "aqi": c["pollution"]["current"],
            "life_expectancy": c["life_expectancy"]["current"],
            "education": c["education"]["current"],
            "military": c["military"]["current"],
            "happiness": c["happiness"]["current"]
        })
        
    return curr_data

if __name__ == "__main__":
    # Test output
    print(json.dumps(get_current_data(), indent=2))
