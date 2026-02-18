from typing import Dict, List

SENIORITY_LEVELS = ["Junior", "Mid-Level", "Senior", "Staff/Principal"]

CHALLENGE_PATTERNS_BY_LEVEL: Dict[str, List[str]] = {
    "Junior": [
        "Loops (for, while)",
        "Arrays and lists manipulation",
        "Conditionals and control flow",
        "String manipulation",
        "Basic functions and parameters",
        "Simple input/output handling",
        "Basic data structures (dict, set)",
    ],
    "Mid-Level": [
        "Recursion",
        "Sorting and searching algorithms",
        "Object-oriented programming",
        "Error handling and validation",
        "Working with collections (map, filter, reduce)",
        "Simple design patterns (e.g. factory, strategy)",
        "Time and space complexity awareness",
    ],
    "Senior": [
        "Trees and graphs",
        "Dynamic programming",
        "Concurrency and async",
        "Design patterns (observer, decorator, etc.)",
        "Performance optimization",
        "API design and contracts",
        "Trade-offs and edge cases",
    ],
    "Staff/Principal": [
        "Scalability and distributed systems",
        "Architecture and boundaries",
        "Trade-offs under constraints",
        "Refactoring and clean code at scale",
        "Cross-cutting concerns",
        "API design and evolution",
        "Testing strategy and quality",
    ],
}


def get_patterns_for_level(seniority: str) -> List[str]:
    return CHALLENGE_PATTERNS_BY_LEVEL.get(seniority, [])
