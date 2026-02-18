# project/pages/login_page.py
from playwright.sync_api import Page, expect

class LoginPage:
    URL = 'https://zimaev.github.io/pom/'
    INVALID_CREDENTIALS_MESSAGE = 'Invalid credentials. Please try again.'
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator('#username')
        self.password_input = page.locator('#password')
        self.login_button = page.locator('#login')
        self.error_message = page.locator('#errorAlert')

    def navigate(self):
        """Открывает страницу логина."""
        self.page.goto('https://zimaev.github.io/pom/')

    def login(self, username: str, password: str):
        """Выполняет вход с заданными учетными данными."""
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def should_be_on_login_page(self) -> None:
        """ Check if there is still login page and url is not changed """
        expect(self.page).to_have_url(LoginPage.URL)

    def get_error_message(self):
        """Возвращает текст сообщения об ошибке."""
        return self.error_message.inner_text()

