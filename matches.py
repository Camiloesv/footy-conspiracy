# Sample season results.
# Each match: home team, away team, home score, away score, misconduct points.
# "misconduct" is the number of yellow-card-style infractions in the match.

MATCHES = [
    # Round 1
    ("Sydney Swans",     "Wagga Wombats",   110, 65,  {"Wagga Wombats": 1}),
    ("Geelong Cats",     "North Knights",    98, 72,  {}),
    ("Brisbane Lions",   "Gold Coast Suns", 105, 80,  {"Gold Coast Suns": 1}),
    ("Melbourne Demons", "Hawthorn Hawks",   89, 84,  {}),
    ("Carlton Blues",    "Essendon Bombers", 95, 92,  {"Essendon Bombers": 2}),
    ("Port Adelaide",    "Richmond Tigers",  88, 81,  {}),

    # Round 2
    ("Wagga Wombats",    "North Knights",    70, 68,  {"Wagga Wombats": 4}),
    ("Sydney Swans",     "Geelong Cats",    101, 99,  {}),
    ("Brisbane Lions",   "Carlton Blues",   102, 91,  {}),
    ("Melbourne Demons", "Port Adelaide",    87, 90,  {"Melbourne Demons": 1}),
    ("Hawthorn Hawks",   "Richmond Tigers",  76, 88,  {}),
    ("Essendon Bombers", "Gold Coast Suns",  93, 71,  {}),

    # Round 3
    ("Wagga Wombats",    "Gold Coast Suns",  68, 64,  {"Wagga Wombats": 2}),
    ("Sydney Swans",     "Brisbane Lions",  104, 97,  {}),
    ("Geelong Cats",     "Melbourne Demons", 95, 88,  {}),
    ("Carlton Blues",    "Hawthorn Hawks",   93, 79,  {}),
    ("Port Adelaide",    "Essendon Bombers", 86, 84,  {"Essendon Bombers": 3}),
    ("Richmond Tigers",  "North Knights",    91, 70,  {}),

    # Round 4
    ("North Knights",    "Wagga Wombats",    77, 60,  {}),
    ("Sydney Swans",     "Melbourne Demons", 99, 90,  {}),
    ("Geelong Cats",     "Carlton Blues",    96, 88,  {}),
    ("Brisbane Lions",   "Hawthorn Hawks",   88, 75,  {}),
    ("Port Adelaide",    "Gold Coast Suns",  94, 66,  {}),
    ("Richmond Tigers",  "Essendon Bombers", 85, 83,  {"Richmond Tigers": 1}),

    # Round 5
    ("Wagga Wombats",    "Hawthorn Hawks",  124, 60,  {}),
    ("Sydney Swans",     "Port Adelaide",    96, 94,  {}),
    ("Geelong Cats",     "Brisbane Lions",   91, 95,  {}),
    ("Carlton Blues",    "Richmond Tigers",  82, 80,  {}),
    ("Melbourne Demons", "North Knights",    93, 70,  {}),
    ("Essendon Bombers", "Gold Coast Suns",  88, 70,  {}),

    # Round 6
    ("Wagga Wombats",    "Essendon Bombers", 75, 73,  {}),
    ("Brisbane Lions",   "Richmond Tigers",  86, 82,  {}),
    ("Carlton Blues",    "Melbourne Demons", 90, 88,  {}),
    ("Hawthorn Hawks",   "North Knights",    79, 71,  {"Hawthorn Hawks": 1}),
    ("Port Adelaide",    "Geelong Cats",     85, 88,  {}),
    ("Sydney Swans",     "Gold Coast Suns", 102, 70,  {}),
]
