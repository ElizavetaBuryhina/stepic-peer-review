link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_page_contains_add_to_cart_button(browser):
    browser.get(link)
    button = browser.find_element_by_class_name('btn-add-to-basket')
    assert button != None, 'button is not found'
    