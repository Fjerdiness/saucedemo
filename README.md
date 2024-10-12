# Project Title

Just to show some skills for possible employer

## Table of Contents

1. [Technologies Used](#technologies-used)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Documentation](#documentation)

## Technologies Used

- **Programming Language**: Python
- **Testing Framework**: pytest
- **Web Automation**: Selenium
- **Libraries**: 
  - See [requirements.txt](requirements.txt) for a complete list of libraries and dependencies.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Python**:
   - Ensure Python 3.x is installed. You can download it from [python.org](https://www.python.org/downloads/).

3. **pip**:
   - Install pip, the package installer for Python, if it’s not already included with your Python installation.

4. **Web Drivers**:
   - **ChromeDriver**: For Chrome users, download it from [chromedriver](https://developer.chrome.com/docs/chromedriver/downloads).
   - **GeckoDriver**: For Firefox users, download it from [GeckoDriver releases](https://github.com/mozilla/geckodriver/releases).

5. **Navigate into the Project Directory**:
   ```bash
   cd <repository-directory>
   ```

6. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   ```

7. **Change Execution Policy (Windows PowerShell)**:
   If you're using PowerShell on Windows, you may need to change the execution policy. Run:
   ```bash
   Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
   ```

8. **Activate the Virtual Environment**:
   - For PowerShell:
     ```bash
     .\venv\Scripts\Activate.ps1
     ```
   - For Command Prompt:
     ```bash
     venv\Scripts\activate
     ```
   - For macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

9. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
- On Windows:
```bash
py -m pytest tests/
```
- On macOS:
```bash
python3 -m pytest tests/
```
- On Linux:
```bash
python3 -m pytest tests/
```

- Use the `-v` flag to run tests in verbose mode and see debug prints:
        
```bash
py -m pytest -v -s tests/
```

- To run a specific test using `pytest`, you can use the following command:

```bash
py -m pytest -v -s tests/%MODULE_NAME%.py::%TEST_CASE_NAME%
```

# Documentation

## Scenario: Valid Login
**Given** the user enters valid credentials  
**When** the user submits the login form  
**Then** the user should be redirected to the inventory page  
**And** the header logo should be visible  

### Parameterized Inputs
- **Username and Password**: 
  - **Input:** 
    - `("standard_user", "secret_sauce")`
    - `("problem_user", "secret_sauce")`
    - `("performance_glitch_user", "secret_sauce")`
    - `("error_user", "secret_sauce")` 
    - `("visual_user", "secret_sauce")` 
  - **Expected Result:** Redirects to the inventory page.

---

## Scenario: Locked Out User Login
**Given** the user enters invalid credentials  
**When** the user submits the login form  
**Then** an error message should be displayed  
**And** the error message container should exist  

### Parameterized Inputs
- **Username and Password**: 
  - **Input:** 
    - `("locked_out_user", "secret_sauce")`  
  - **Expected Result:** Displays the message "Epic sadface: Sorry, this user has been locked out."

---

## Scenario: No Username Login
**Given** the user navigates to the login page  
**When** the user attempts to log in with no username  
**Then** the error message container should be visible  
**And** the error message should indicate "Epic sadface: Username is required"  

---

## Scenario: No Password Login
**Given** the user navigates to the login page  
**When** the user attempts to log in with no password  
**Then** the error message container should be visible  
**And** the error message should indicate "Epic sadface: Password is required"  

---

## Scenario: Non-Existent Login
**Given** the user navigates to the login page  
**When** the user attempts to log in with non-existent credentials  
**Then** the error message container should be visible  
**And** the error message should indicate "Epic sadface: Sorry, this user does not exist."  

---

## Scenario: Sorting by Letter (Reverse)
**Given** the user is logged in  
**When** the user selects the "Z to A" option from the dropdown menu  
**Then** the product titles should be sorted in descending order (Z to A)  

---

## Scenario: Sorting by Letter
**Given** the user is logged in  
**When** the user selects the "Z to A" option  
**Then** the product titles should be sorted in descending order  
**And** the user selects the "A to Z" option  
**Then** the product titles should be sorted in ascending order (A to Z)  

---

## Scenario: Sorting by Price (Reverse)
**Given** the user is logged in  
**When** the user selects the "Low to High" option  
**Then** the product prices should be sorted in ascending order (Low to High)  

---

## Scenario: Sorting by Price
**Given** the user is logged in  
**When** the user selects the "High to Low" option  
**Then** the product prices should be sorted in descending order (High to Low)  

---

## Scenario: Cart Button Visibility
**Given** the user is logged in  
**Then** the cart button should be visible  

---

## Scenario: Burger Menu Button Visibility
**Given** the user is logged in  
**Then** the burger menu button should be visible  

---

## Scenario: Adding All Items to Cart
**Given** the user is logged in  
**When** the user adds all available items to the cart  
**Then** the cart badge should reflect the total number of items added  

---

## Scenario: Updating Cart Badge
**Given** the user is logged in  
**When** the user adds a specified number of items to the cart  
**Then** the cart badge should update to reflect the correct number of items  

---

## Scenario: Filters Dropdown Visibility
**Given** the user is logged in  
**And** the user adds an item to the cart  
**Then** the filters dropdown menu should be visible and functional  

---

## Scenario: Burger Menu Buttons Visibility
**Given** the user is logged in  
**Then** all burger menu buttons should be visible  

---

## Scenario: Clicking Burger Menu Items
**Given** the user is logged in  
**When** the user clicks the "All Items" button in the burger menu  
**Then** the user should be redirected to the all items page  

---

## Scenario: Going to the Cart
**Given** the user is logged in  
**And** the user adds an item to the cart  
**When** the user navigates to the cart  
**Then** the cart page should display the correct items  

---

## Scenario: Continue Shopping
**Given** the user is logged in  
**And** the user adds an item to the cart  
**When** the user navigates to the cart  
**And** the user clicks on the continue shopping button  
**Then** the user should be redirected to the inventory page  

---

## Scenario: Valid Checkout
**Given** the user is logged in  
**And** the user adds an item to the cart  
**When** the user proceeds to checkout  
**And** the user fills in valid checkout information  
**Then** the checkout step 1 should be successful  
**And** the user should be able to finish the checkout process  

---

## Scenario: Invalid Checkout
**Given** the user is logged in  
**And** the user adds an item to the cart  
**When** the user proceeds to checkout  
**And** the user fills in invalid checkout information  
**Then** the checkout step 1 should fail  

### Parameterized Inputs
- **Checkout Information**: 
  - **Input Variants**:
    - `("", "ValidLastName", "111")`  
      - **Expected Error Message:** "Error: First Name is required"
    - `("ValidFirstName", "", "111")`  
      - **Expected Error Message:** "Error: Last Name is required"
    - `("ValidFirstName", "ValidLastName", "")`  
      - **Expected Error Message:** "Error: Postal Code is required"

---

## Scenario: Checkout Button Visibility
**Given** the user is logged in  
**And** the user adds an item to the cart  
**When** the user navigates to the cart  
**And** the user proceeds to checkout  
**Then** the checkout button should not be visible  

---

## Scenario: Cancel Checkout
**Given** the user is logged in  
**And** the user adds an item to the cart  
**When** the user proceeds to checkout  
**And** the user cancels the checkout  
**Then** the user should be redirected back to the cart page  

---

## Scenario: Social Media Links
**Given** the user is logged in  
**When** the user clicks the Twitter link  
**Then** the user should be redirected to the Twitter page  
**When** the user clicks the Facebook link  
**Then** the user should be redirected to the Facebook page  
**When** the user clicks the LinkedIn link  
**Then** the user should be redirected to the LinkedIn page  

## Non-Functional Test Cases

### Scenario: Page Load Performance
**Given** the user navigates to the inventory page  
**Then** the page should load within 2 seconds  

---

### Scenario: Responsiveness
**Given** the user resizes the browser window  
**Then** the layout should adjust correctly for all screen sizes  

---

### Scenario: Security
**Given** the user is logged in  
**When** the user attempts to access the admin page  
**Then** the user should be redirected to the home page with an "Access Denied" message  

---

### Scenario: Compatibility
**Given** the user opens the inventory page in different browsers  
**Then** the page should render correctly in Chrome, Firefox, and Safari  

---

### Scenario: Non valid URL
**Given** the user opens the wrong link
**Then** should be opened 404 page 
