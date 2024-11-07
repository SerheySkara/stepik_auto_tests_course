def test_add_to_cart_button(browser):
    # Открываем страницу товара
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    
    # Ищем кнопку добавления в корзину
    button = browser.find_elements_by_css_selector(".btn-add-to-basket")
    assert button, "Button 'Add to cart' not found on the page"

