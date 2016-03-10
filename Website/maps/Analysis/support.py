DEFAULT_KEY = None

colors = {0: "909090", 1:"E50008", 2: "C8011E", 3: "AB0235", 4:"8F034C", 5: "720463", 6: "55057A", 7:"390691", 8: "1C07A8", 9:"0008BF"}

color_matrix = {
    ("low", DEFAULT_KEY): "#8F034C",
    ("med", DEFAULT_KEY): "#C8011E",
    ("high", DEFAULT_KEY): "#E50008",
    ("low", "low") : "#8F034C",  
    ("med", "low") : "#C8011E", 
    ("high", "low") : "#E50008", 
    ("low", "med") : "#390691",
    ("med", "med") : "#720463", 
    ("high", "med") : "#AB0235", 
    ("low", "high") : "#0008BF",   
    ("med", "high") : "#1C07A8", 
    ("high", "high") : "#720463",
    None:  "#B5B5B5"
}

index_matrix = {
    0 : "low",
    1: "med",
    2: "high",
}

scatter_matrix = {
    ("low", DEFAULT_KEY): 0,
    ("med", DEFAULT_KEY): 1,
    ("high", DEFAULT_KEY): 2,
    ("low", "low") : 0,  
    ("med", "low") : 1, 
    ("high", "low") : 2, 
    ("low", "med") : 3,
    ("med", "med") : 4, 
    ("high", "med") : 5, 
    ("low", "high") : 6,   
    ("med", "high") : 7, 
    ("high", "high") : 8,
}

