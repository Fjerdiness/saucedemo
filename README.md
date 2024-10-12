# How To:

0. Clone the repository and install Python and pip.
1. Navigate into the project directory:
   - `cd saucedemo`
2. Create a virtual environment:
   - `python -m venv venv`
3. If you're using PowerShell on Windows, you may need to change the execution policy. Run:  
   - `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned`
4. Activate the virtual environment:
   - For PowerShell:  
     - `.\venv\Scripts\Activate.ps1`
   - For Command Prompt:  
     - `venv\Scripts\activate`
   - For macOS/Linux:  
     - `source venv/bin/activate`
5. Install the required packages:
   - `pip install -r requirements.txt`
6. Run the tests to ensure everything is set up correctly:
   - Windows:  
     - `py -m pytest tests/`
   - macOS:  
     - `python3 -m pytest tests/`
   - Linux:  
     - `python3 -m pytest tests/`

---

# Cucumber Style Documentation

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
