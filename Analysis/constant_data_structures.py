valid_headers = ['Community Area','Community Area Name','Birth Rate','General Fertility Rate','Low Birth Weight','Prenatal Care Beginning in First Trimester','Preterm Births','Teen Birth Rate','Assault (Homicide)','Breast cancer in females','Cancer (All Sites)','Colorectal Cancer','Diabetes-related','Firearm-related','Infant Mortality Rate','Lung Cancer','Prostate Cancer in Males','Stroke (Cerebrovascular Disease)','Childhood Blood Lead Level Screening','Childhood Lead Poisoning','Gonorrhea in Females','Gonorrhea in Males','Tuberculosis','Below Poverty Level','Crowded Housing','Dependency','No High School Diploma', 'Per Capita Income', 'Unemployment']

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