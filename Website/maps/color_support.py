DEFAULT_KEY = None

color_matrix = {
    ("low", DEFAULT_KEY): "#8F034C",
    ("med", DEFAULT_KEY): "#C8011E",
    ("high", DEFAULT_KEY): "#E50008",
    ("low", "low") : "#8F034C",  
    ("med", "low") : "#390691", 
    ("high", "low") : "#0008BF", 
    ("low", "med") : "#C8011E",
    ("med", "med") : "#720463", 
    ("high", "med") : "#1C07A8", 
    ("low", "high") : "#E50008",   
    ("med", "high") : "#AB0235", 
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

scatter_color_list = ["#8F034C", "#390691", "#0008BF", "#C8011E","#720463","#1C07A8","#E50008","#AB0235","#55057A"]