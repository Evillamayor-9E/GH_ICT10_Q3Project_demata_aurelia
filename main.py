from pyscript import display, document  # pyright: ignore[reportMissingImports]

def checkRegistration(e):
    e.preventDefault()  # Prevent form from reloading the page
    
    online_reg = document.getElementById('onlineReg').checked
    medical_clearance = document.getElementById('medicalClearance').checked
    grade_level = document.getElementById('gradeLevel').value.strip()
    section = document.getElementById('section').value.strip()
    
    result_div = document.getElementById('result')
    
    if not grade_level or not section:
        result_div.className = 'result error'
        result_div.textContent = 'Please select your grade level and section.'
        result_div.style.display = 'block'
        return
    
    is_eligible = check_eligibility(online_reg, medical_clearance, grade_level)
    
    if is_eligible:
        team = assign_team(grade_level, section)
        team_image = get_team_image(team)
        result_div.className = 'result success'
        result_div.innerHTML = f'''
            <div style="line-height: 1.8;">
                <strong style="font-size: 18px;">🎉 Congratulations!</strong><br>
                You are eligible to join the Intramurals!<br>
                <img src="{team_image}" alt="{team}" style="max-width: 120px; margin: 15px 0; border-radius: 8px;"><br>
                <strong>Your Assigned Team: {team}</strong>
            </div>
        '''
        result_div.style.display = 'block'
    else:
        missing_items = get_missing_requirements(online_reg, medical_clearance, grade_level)
        result_div.className = 'result error'
        result_div.innerHTML = f'''
            <div style="line-height: 1.8;">
                <strong style="font-size: 16px;">❌ Not Eligible</strong><br>
                {missing_items}
            </div>
        '''
        result_div.style.display = 'block'

def check_eligibility(online_reg, medical_clearance, grade_level):
    """
    Determine if student is eligible for intramurals
    Conditions:
    - Must be registered online
    - Must have medical clearance
    - Must be in grades 7-10
    """
    grade_num = int(grade_level.split()[-1])
    return online_reg and medical_clearance and (7 <= grade_num <= 10)

def get_missing_requirements(online_reg, medical_clearance, grade_level):
    """Generate message listing missing requirements"""
    missing = []
    
    if not online_reg:
        missing.append('Please register online for the Intramurals.')
    
    if not medical_clearance:
        missing.append('Please secure a medical clearance from the clinic.')
    
    grade_num = int(grade_level.split()[-1])
    if grade_num < 7 or grade_num > 10:
        missing.append('Only students in grades 7-10 are eligible for Intramurals.')
    
    return '<br>'.join(missing)

def assign_team(grade_level, section):
    """
    Assign student to an intramurals team based on their grade and section
    
    Teams:
    - Red Bulldogs: 7R, 8J, 9R, 10T
    - Blue Bears: 7E, 8E, 8R, 9E, 10R
    - Yellow Tigers: 7T, 8S, 9T, 10E
    - Green Hornets: 7S, 8T, 9S, 10S
    """
    grade = grade_level.split()[-1]
    section_letter = section[0].upper()
    student_code = grade + section_letter
    
    team_mapping = {
        '7R': 'Red Bulldogs', '8J': 'Red Bulldogs', '9R': 'Red Bulldogs', '10T': 'Red Bulldogs',
        '7E': 'Blue Bears', '8E': 'Blue Bears', '8R': 'Blue Bears', '9E': 'Blue Bears', '10R': 'Blue Bears',
        '7T': 'Yellow Tigers', '8S': 'Yellow Tigers', '9T': 'Yellow Tigers', '10E': 'Yellow Tigers',
        '7S': 'Green Hornets', '8T': 'Green Hornets', '9S': 'Green Hornets', '10S': 'Green Hornets'
    }
    
    return team_mapping.get(student_code, 'Blue Bears')

def get_team_image(team_name):
    team_images = {
        'Red Bulldogs': 'images/red-bulldogs.jpeg',
        'Blue Bears': 'images/blue-bears.jpg',
        'Yellow Tigers': 'images/yellow-tigers.jpeg',
        'Green Hornets': 'images/green-hornets.jpeg'
    }
    return team_images.get(team_name, 'images/blue-bears.jpeg')

# Add event listener to handle form submission
document.getElementById("registrationForm").addEventListener("submit", checkRegistration)
    
