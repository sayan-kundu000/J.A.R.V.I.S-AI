import random

def get_country_rankings():
    """
    Returns expanded mock data for top 15 countries with historical and current comparisons.
    Factors: GDP, Population, AQI, Life Expectancy, Education, Military, Happiness.
    """
    countries = [
        "USA", "China", "India", "Japan", "Germany", 
        "UK", "France", "Brazil", "Italy", "Canada", 
        "Russia", "South Korea", "Australia", "Spain", "Mexico"
    ]
    
    data = []
    
    for c in countries:
        # Base values (Current)
        if c == "USA":
            gdp, pop, aqi, life, edu, mil, hap = 25400, 333, 35, 78.8, 0.92, 98, 7.2
        elif c == "China":
            gdp, pop, aqi, life, edu, mil, hap = 17900, 1412, 85, 77.3, 0.82, 95, 5.8
        elif c == "India":
            gdp, pop, aqi, life, edu, mil, hap = 3400, 1428, 110, 70.1, 0.65, 88, 4.2
        elif c == "Japan":
            gdp, pop, aqi, life, edu, mil, hap = 4200, 125, 25, 84.6, 0.93, 75, 6.1
        elif c == "Germany":
            gdp, pop, aqi, life, edu, mil, hap = 4000, 83, 28, 81.3, 0.94, 70, 7.0
        else:
            gdp = round(random.uniform(1200, 3100), 1)
            pop = round(random.uniform(40, 215), 1)
            aqi = round(random.uniform(20, 65), 1)
            life = round(random.uniform(65, 80), 1)
            edu = round(random.uniform(0.5, 0.9), 2)
            mil = round(random.uniform(30, 65), 1)
            hap = round(random.uniform(4.0, 6.5), 1)
            
        # Mock historical growth/decline (approx 15 years ago)
        data.append({
            "country": c,
            "gdp": {"current": gdp, "historical": round(gdp * random.uniform(0.6, 0.85), 1)},
            "population": {"current": pop, "historical": round(pop * random.uniform(0.85, 0.98), 1)},
            "pollution": {"current": aqi, "historical": round(aqi * random.uniform(1.1, 1.4), 1)}, # AQI was worse usually
            "life_expectancy": {"current": life, "historical": round(life - random.uniform(2, 5), 1)},
            "education": {"current": edu, "historical": round(edu - 0.1, 2)},
            "military": {"current": mil, "historical": round(mil * random.uniform(0.8, 1.1), 1)},
            "happiness": {"current": hap, "historical": round(hap + random.uniform(-0.5, 0.5), 1)}
        })
        
    return data
