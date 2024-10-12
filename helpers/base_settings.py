
from typing import Tuple


BASE_URL = "https://www.saucedemo.com/"
INVENTORY_URL = BASE_URL + "inventory.html"
CART_URL = BASE_URL + "cart.html"
CHECKOUT_1_URL = BASE_URL + "checkout-step-one.html"
CHECKOUT_2_URL = BASE_URL + "checkout-step-two.html"
CHECKOUT_COMPLETE_URL = BASE_URL + "checkout-complete.html"

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

def get_credentials(user_type: str)  -> Tuple[str, str]:
    password = NON_VALID_CREDS.get(user_type)
    if password is not None:
        return user_type, password  
    return None, None