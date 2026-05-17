ETHICAL_HACKING_KNOWLEDGE = {
    "nmap": "Nmap is an open-source tool used for network discovery and security auditing. It helps identify live hosts, open ports, and services running on a network.",
    "penetration test": "Penetration testing, or ethical hacking, is the authorized simulation of cyberattacks to evaluate the security of a system. It follows phases like reconnaissance, scanning, gaining access, maintaining access, and reporting.",
    "vulnerability": "A vulnerability is a weakness in a system that could be exploited. Ethical hackers use tools like Nessus or OpenVAS to identify these flaws to patch them before malicious actors can exploit them.",
    "phishing": "Phishing is a social engineering attack often used to steal user data. Ethical hackers run phishing simulations to train employees on how to recognize and report suspicious emails.",
    "sql injection": "SQL Injection (SQLi) is a code injection technique. Ethical hackers test for SQLi to ensure web applications sanitize user input, preventing unauthorized database access.",
    "white hat": "White hat hackers are ethical security professionals who use their skills to improve security by finding and fixing vulnerabilities with explicit permission.",
    "red hat": "Red hat hackers usually act as Linux/enterprise security experts or vigilant hackers who actively stop malicious attacks (sometimes using offensive measures like taking down the attacker's system).",
    "red team": "Red teaming involves simulating full-spectrum, multi-layered cyberattacks to test an organization's detection and response capabilities.",
    "blue team": "The blue team is the internal cybersecurity team responsible for defending against cyberattacks and proactively responding to incidents.",
    "blue hat": "Blue hat hackers are outside security professionals invited by organizations (like Microsoft) to bug-test software before it is released.",
    "grey hat": "Grey hat hackers may violate ethical standards or principles by exploring systems without permission, but without malicious intent, often reporting the vulnerabilities later.",
    "black hat": "Black hat hackers are malicious actors who break into systems for personal gain, data theft, or sabotage. Ethical hacking exists precisely to counteract black hat actions.",
    "metasploit": "The Metasploit Framework is a powerful tool for penetration testing that helps security teams verify vulnerabilities and manage security assessments."
}

def process_cyber_query(query):
    query_lower = query.lower()
    
    # Check if the query is related to ethical hacking
    keywords = ["hack", "security", "penetration", "nmap", "vulnerability", "phishing", "malware", "cyber"]
    # Check for hats
    hats = ["white hat", "red hat", "blue hat", "grey hat", "black hat"]
    
    is_cyber = any(word in query_lower for word in keywords) or any(hat in query_lower for hat in hats)
    
    if not is_cyber:
        return None
        
    for key, response in ETHICAL_HACKING_KNOWLEDGE.items():
        if key in query_lower:
            return response
            
    # Generic ethical hacking response
    return "I am equipped with ethical hacking and cybersecurity knowledge. I can provide defensive strategies, explain vulnerabilities, and discuss penetration testing methodologies to help secure systems from threats."
