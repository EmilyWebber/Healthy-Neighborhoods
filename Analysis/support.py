valid_headers = ['Community Area','Community Area Name','Birth Rate','General Fertility Rate','Low Birth Weight','Prenatal Care Beginning in First Trimester','Preterm Births','Teen Birth Rate','Assault (Homicide)','Breast cancer in females','Cancer (All Sites)','Colorectal Cancer','Diabetes-related','Firearm-related','Infant Mortality Rate','Lung Cancer','Prostate Cancer in Males','Stroke (Cerebrovascular Disease)','Childhood Blood Lead Level Screening','Childhood Lead Poisoning','Gonorrhea in Females','Gonorrhea in Males','Tuberculosis','Below Poverty Level','Crowded Housing','Dependency','No High School Diploma', 'Per Capita Income', 'Unemployment']

color_matrix = {
    ("low", "low") : 1,
    ("med", "low") : 2,
    ("high", "low") : 3,
    ("low", "med") : 4,
    ("med", "med") : 5,
    ("high", "med") : 6,
    ("low", "high") : 7,
    ("med", "high") : 8,
    ("high", "high") : 9
}

index_matrix = {
    0 : "low",
    1: "med",
    2: "high",
}