
BASE_URL = "https://www.saucedemo.com/"
INVENTORY_URL = BASE_URL + "inventory.html"
CART_URL = BASE_URL + "cart.html"
CHECKOUT_1_URL = BASE_URL + "checkout-step-one.html"
CHECKOUT_2_URL = BASE_URL + "checkout-step-two.html"
CHECKOUT_COMPLETE_URL = BASE_URL + "checkout-complete.html"
SAUCELABS_URL = "https://saucelabs.com/"

XITTER_URL = "https://x.com/saucelabs"
FB_URL = "https://www.facebook.com/saucelabs"
LINKEDIN_URL = "https://www.linkedin.com/"

NON_VALID_CREDS = {
    "locked_out_user": "secret_sauce", # Locked out user
}

VALID_CREDS = { 
    "standard_user": "secret_sauce",   
    "problem_user": "secret_sauce",    
    "performance_glitch_user": "secret_sauce",
    "error_user": "secret_sauce",      # Expect checkout error
    "visual_user": "secret_sauce",      # Expect visual errors
}

LOGIN_ERRORS_STR = [
    "Epic sadface: Username is required",
    "Epic sadface: Password is required",
    "Epic sadface: Sorry, this user has been locked out.",
    "Epic sadface: Username and password do not match any user in this service",
]


CHECKOUT_ERRORS_STR = [
    "Error: First Name is required",
    "Error: Last Name is required",
    "Error: Postal Code is required",
]

INVALID_CHECKOUT_INFO_STR = [
    ("", "ValidLastName", "111", CHECKOUT_ERRORS_STR[0]),
    ("ValidFirstName", "", "111", CHECKOUT_ERRORS_STR[1]), 
    ("ValidFirstName", "ValidLastName", "", CHECKOUT_ERRORS_STR[2]),
]