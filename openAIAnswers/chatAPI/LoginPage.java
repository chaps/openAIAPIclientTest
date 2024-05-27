public class LoginPage {

    private WebDriver driver;

    public LoginPage(WebDriver driver) {
        this.driver = driver;
    }

    public WebElement getLoginTextInput() {
        return driver.findElement(By.id("login-username"));
    }

    public WebElement getPasswordTextInput() {
        return driver.findElement(By.id("login-password"));
    }

    public WebElement getLoginSubmitButton() {
        return driver.findElement(By.xpath("//button[contains(text(),'Log In')]"));
    }

    public void enterUsername(String username) {
        getLoginTextInput().sendKeys(username);
    }

    public void enterPassword(String password) {
        getPasswordTextInput().sendKeys(password);
    }

    public void clickLoginSubmit() {
        getLoginSubmitButton().click();
    }

}