from pyscript import display, document

#SW1--------------
Members = ["Sponge Bob", "Patrick Star", "Squidward", "Sandy Cheeks", "Mr. Crabs", "Plankton", "Karen", "Hermando"]

def check_membership(e):
    document.getElementById("output1").innerHTML = ""

    fname = document.getElementById("first_name").value
    lname = document.getElementById("last_name").value

    applicant_name = str(fname + " " + lname)

    check = applicant_name.title() in Members

    verified = "Congratulations" + " " + applicant_name + "!" + " " + "Welcome to the OBMC Literature Club!!!!"
    not_verified = "Whoah" + " " + applicant_name + ", " + "your not on the list....sign-up first"

    display({
        True: verified,
        False: not_verified
    }[check], target="output1")

#SKILLS TEST------------------------------
non_metals = {
"H": ('Hydrogen', 1, 1.008),
"HE": ('Helium', 2, 4.0026),
"C": ('Carbon', 6, 12.011),
"N": ('Nitrogen', 7, 14.007),
"O": ('Oxygen', 8, 15.999),
"F": ('Fluorine', 9, 18.998),
"NE": ('Neon', 10, 20.180),
"P": ('Phosphorus', 15, 30.974),
"S": ('Sulfur', 16, 32.06),
"Cl": ('Chlorine', 17, 35.45),
"AR": ('Argon', 18, 39.948),
"SE": ('Selenium', 34, 78.971),
"BR": ('Bromine', 35, 79.904),
"KR": ('Krypton', 36, 83.798),
"I": ('Iodine', 53, 126.90),
"XE": ('Xenon', 54, 131.29),
"AT": ('Astatine', 85, 210),
"RN": ('Radon', 86, 222),
"TS": ('Tennessine', 117, 294),
"OG": ('Oganesson', 118, 294)}

#Fuction to search 4 Element
def Search_Element(e):
    #Get the input from HTML

    element_1 = document.getElementById("element1").value.upper()
    # retrive information from the dictionary

    result = non_metals.get(element_1, ('Element not found',"-","-"))
    #display the result in HTML
    document.getElementById("symbol").innerText = element_1
    document.getElementById("name").innerText = result[0]
    document.getElementById("num").innerText = result[1]
    document.getElementById("mass").innerText = result[2]

#Drill2--------------------------------

# Members organized by grade level
Grade_7 = [
    "Mister Crabs", "Sponge bob", "Sandy Cheeks",
    "Squidward", "Plankton", "Patrick Star",
    "Ms. Puff", "Gumball"
]

Grade_8 = [
    "Darwin", "Ananais", "Richard", "Penny",
    "Peter Parker", "Gwen Stacy", "Mary Jane",
    "Ben Riley", "Eddie Brock", "Bruce wane"
]

Grade_9 = [
    "Jason Todd", "Dick Grayson"
]

Grade_10 = [
    "Damian Wane", "Freddy", "Vanessa"
]


# Function triggered by the Check button
def check_membership(event=None) -> None:

    # Get the names from the HTML input fields
    first_name = document.getElementById(
        "first_name"
    ).value.strip().title()

    last_name = document.getElementById(
        "last_name"
    ).value.strip().title()

    output = document.getElementById("output1")

    # Make sure both fields are completed
    if not first_name or not last_name:
        output.innerHTML = """
            <div style="color: #9b4050;">
                ✦ ENTRY INCOMPLETE ✦<br>
                Please enter both your first and last name.
            </div>
        """
        return

    # Combine the names
    full_name = f"{first_name} {last_name}"

    # Converted grade lists into sets
    grade_7 = set(Grade_7)
    grade_8 = set(Grade_8)
    grade_9 = set(Grade_9)
    grade_10 = set(Grade_10)

    # Combine all existing members
    master_set = (
        grade_7 | grade_8 | grade_9 | grade_10
    )

    # Check whether the person is already a member
    if full_name in master_set:
        output.innerHTML = f"""
            <div style="color: #667da8;">
                ✦ MEMBER IDENTIFIED ✦<br><br>
                Welcome back, {full_name}!<br>
                Your name is already in the Literature Club registry.
            </div>
        """
    else:
        # Add the new member to the master set
        master_set.add(full_name)

        # Sort names alphabetically for a neat display
        formatted_members_list = "".join(
            f"<li>{name}</li>"
            for name in sorted(master_set)
        )

        total_count = len(master_set)


