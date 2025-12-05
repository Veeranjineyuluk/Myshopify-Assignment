from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    
    page.goto("https://sauce-demo.myshopify.com/")
    page.wait_for_timeout(3000)
    
    page.get_by_text("Log In").click()
    page.wait_for_timeout(3000)
    
    page.get_by_label("Email Address").fill("veeranjineyuluk123@gmail.com")
    page.get_by_label("Password").fill("Veera@123")
    
    page.wait_for_timeout(3000)
    page.locator("//input[@value='Sign In']").click()    
    
    
    page.locator("#main-menu >> text=Home").click()
    
    page.wait_for_timeout(3000)
    
    page.get_by_text("Grey jacket").click()
    
    
    page.locator("#add").click()
    page.wait_for_timeout(3000)
    
    page.get_by_text("My Cart").first.click()
    
    page.wait_for_timeout(3000)
    cart_text = page.locator("body").inner_text()
    
    
    """if "Grey jacket".lower() in cart_text.lower():
        print(" SUCCESS: Product added to cart successfully!")
    else:
        print("FAILED: Product not found in cart.")
    page.wait_for_timeout(3000)"""
    
    assert "Grey jacket".lower() in cart_text.lower(), "Product not found in cart!"
    print("SUCCESS: Product added to cart successfully!")
    
    browser.close()
    
    
    
    
    