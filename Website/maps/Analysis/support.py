DEFAULT_KEY = None

color_matrix = {
    ("low", DEFAULT_KEY): 1,
    ("med", DEFAULT_KEY): 2,
    ("high", DEFAULT_KEY): 3,
    ("low", "low") : "#BCC6CC",
    ("med", "low") : "#98AFC7",
    ("high", "low") : "#6D7B8D",
    ("low", "med") : "#657383",
    ("med", "med") : "#616D7E",
    ("high", "med") : "#646D7E",
    ("low", "high") : "#566D7E",
    ("med", "high") : "#737CA1",
    ("high", "high") : "#4863A0"
}

index_matrix = {
    0 : "low",
    1: "med",
    2: "high",
}