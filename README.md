**UI Test – Add Product to Cart**
This is a basic Playwright test that opens the website, logs in, selects a product, adds it to the cart, and checks if the item was added successfully.

**How to set up the environment**

>>Install Python 3
>>Install Playwright:
                          **pip install playwright
                         **playwright install

>>Make sure all dependencies are installed before running the script.

**How to run the test**
>>Save the script as test_add_to_cart.py and run:
                            **test_add_to_cart.py
>>The browser will open and the test will run step by step.

**What the test does**
>>Opens the Sauce Demo Shopify page
>>Logs in using email and password
>>Goes to the Home page
>>Clicks on Grey jacket
>>Opens the product page
>>Adds the product to the cart
>>Opens the cart
>>Checks if the product name appears in the cart

**Assumptions**
>>The product Grey jacket is available on the Home page
>>Login works without OTP
>>The "Add to cart" button uses the selector " #add  "
>>The cart page displays the product name as text

**Challenges faced**
>>Some elements took time to load, so I had to use waits
>>Shopify themes change, so selectors may not always be consistent
>>Locators like get_by_text may match multiple elements sometimes

**What I would improve with more time**
>>Replace time-based waits with proper Playwright waits
>>Use dynamic product selection instead of hardcoding the name
>>Add more validations like quantity or price checks
>>Convert the script into a pytest format
>>Use a Page Object Model to organize the code better

**Test design summary**
>>I kept the flow very simple, using direct locators and one main assertion.
>>The goal was to complete the required flow clearly and make the script easy to read for a beginner.
