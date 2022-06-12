# test_my_application.py
def test_example_open_page(page):
    # Go to https://www.tsum.ru/
    page.goto("https://www.tsum.ru/")
    assert page.inner_text('h1').startswith('ИНТЕРНЕТ')
    page.wait_for_timeout(300)


def test_goto_men(page):
    test_example_open_page(page)
    # Click top-main-menu >> text=Мужское
    # with page.expect_navigation(url="https://www.tsum.ru/men/"):
    with page.expect_navigation(url="https://www.tsum.ru/men/"):
        page.locator("top-main-menu >> text=Мужское").click()
    assert page.url == "https://www.tsum.ru/men/"


def test_goto_gucci(page):
    page.goto(url="https://www.tsum.ru/men/")
    # Click diginetica-suggest svg
    page.locator("diginetica-suggest svg").click()
    # Fill [placeholder="Поиск"]
    page.locator("[placeholder=\"Поиск\"]").fill("gucci")
    # Press Enter
    # with page.expect_navigation(url="https://www.tsum.ru/catalog/search/?q=gucci"):
    with page.expect_navigation(url="https://www.tsum.ru/catalog/search/?q=gucci"):
        page.locator("[placeholder=\"Поиск\"]").press("Enter")
    # 0× click
    assert page.inner_text("h1") == "Поиск: gucci"
    page.wait_for_timeout(300)


def test_select_categories(page):
    page.goto(url="https://www.tsum.ru/catalog/search/?q=gucci")
    with page.expect_navigation():
        page.locator("#catalog >> text=Кеды").first.click()
    assert page.url == "https://www.tsum.ru/catalog/women-sportivnaya-obuv-kedy-19217/?q=gucci"


def test_select_shoes(page):
    page.goto(url="https://www.tsum.ru/catalog/women-sportivnaya-obuv-kedy-19217/?q=gucci")
    with page.expect_navigation():
        page.locator("text=GucciКожаные кеды New Ace71 650 ₽ >> p").first.click()

    assert page.inner_text("h1") == "Кожаные кеды New Ace"


def test_select_shoes(page):
    page.goto(url="https://www.tsum.ru/catalog/women-sportivnaya-obuv-kedy-19217/?q=gucci")
    with page.expect_navigation():
        page.locator("text=GucciКожаные кеды New Ace71 650 ₽ >> p").first.click()

    assert page.inner_text("h1") == "Кожаные кеды New Ace"


def test_add_to_cart(page):
    page.goto(url="https://www.tsum.ru/product/5506054-kozhanye-kedy-new-ace-gucci-belyi/")
     # Click [data-testid="AddProductToCart"]
    page.locator("[data-testid=\"AddProductToCart\"]").click()
        
    with page.expect_navigation():
        page.locator("[data-testid=\"GoToCart\"]").click()
    page.wait_for_timeout(300)
    assert page.inner_text("h1").startswith("Корзина")


def test_goto_cart(page):
    page.goto(url="https://www.tsum.ru")
    with page.expect_navigation():
        page.locator("img[alt=\"Корзина\"]").click()
    assert page.inner_text("h1").startswith("Корзина")


def test_delete_from_cart(page):
    test_add_to_cart(page)
    # Click text=Удалить
    page.locator("text=Удалить").click()
    page.wait_for_timeout(1300)
    assert page.inner_text("h1") == "Корзина" #with no count
