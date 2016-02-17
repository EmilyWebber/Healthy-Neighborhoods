L = "l"
M = "m"
H = "h"

color_matrix = {
    ("l", "l") : 1,
    ("m", "l") : 2,
    ("h", "l") : 3,
    ("l", "m") : 4,
    ("m", "m") : 5,
    ("h", "m") : 6,
    ("l", "h") : 7,
    ("m", "h") : 8,
    ("h", "h") : 9
}



print (color_matrix[(H,L)])