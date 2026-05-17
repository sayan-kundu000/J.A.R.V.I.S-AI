import math
import re

def process_calculator_query(query):
    """
    A mathematical evaluator simulating Jarvis calculating formulas across science and economics.
    """
    query_lower = query.lower().strip()
    
    # Detect Economic formulas
    if "compound interest" in query_lower:
        return "To calculate compound interest linearly, the economic formula is: A = P(1 + r/n)^(nt). (P=Principal, r=Rate, n=Compounds/Yr, t=Years)."
    if "gdp" in query_lower and "formula" in query_lower:
        return "The standard economic calculation for Gross Domestic Product is: GDP = C(Consumption) + I(Investment) + G(Government Spending) + (X(Exports) - M(Imports))."
    if "gravity" in query_lower and "formula" in query_lower:
        return "Newton's Law of Universal Gravitation is F = G * (m1 * m2) / r^2."
        
    # Standard Math catching
    if "calculate" in query_lower or "what is" in query_lower or "solve" in query_lower:
        # Strip out conversational words
        expr = query_lower.replace("calculate", "").replace("what is", "").replace("solve", "").strip()
        
        # Restrict to safe math strings
        expr_clean = re.sub(r'[^0-9+\-*/().%^ ]', '', expr)
        expr_clean = expr_clean.replace("^", "**") # Handle exponents
        
        if expr_clean.strip():
            try:
                # Highly restricted eval context for safety
                safe_dict = {
                    "sin": math.sin, "cos": math.cos, "tan": math.tan,
                    "sqrt": math.sqrt, "pi": math.pi, "e": math.e,
                    "log": math.log10, "ln": math.log
                }
                result = eval(expr_clean, {"__builtins__": None}, safe_dict)
                # Format to avoid mega long floats
                if isinstance(result, float):
                    result = round(result, 6)
                return f"The calculated result is: {result}"
            except Exception:
                pass
                
    return None
