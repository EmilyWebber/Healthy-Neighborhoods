DEFAULT_KEY = None

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
    ("high", "high") : "#55057A",
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

scatter_color_list = ["#8F034C", "#C8011E", "#E50008", "#390691","#720463","#AB0235","#0008BF","#1C07A8","#55057A"]