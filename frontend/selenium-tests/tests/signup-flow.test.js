const { Builder, By, until } = require("selenium-webdriver");
require("chromedriver");
const assert = require("assert");

describe("KRINTERIOR Signup Flow", function () {
  this.timeout(60000);

  let driver;

  before(async () => {
    driver = await new Builder().forBrowser("chrome").build();
  });

  after(async () => {
    await driver.quit();
  });

  it("should signup successfully", async () => {

    // Generate unique email every run
    const uniqueEmail = `test${Date.now()}@gmail.com`;

    await driver.get("http://localhost:3000/signup");

    await driver.wait(
      until.elementLocated(By.css('[data-testid="name-input"]')),
      10000
    );

    await driver.findElement(
      By.css('[data-testid="name-input"]')
    ).sendKeys("Selenium Test");

    await driver.findElement(
      By.css('[data-testid="signup-email-input"]')
    ).sendKeys(uniqueEmail);

    await driver.findElement(
      By.css('[data-testid="signup-password-input"]')
    ).sendKeys("password123");

    await driver.findElement(
      By.css('[data-testid="signup-submit-btn"]')
    ).click();

    await driver.wait(
      until.urlContains("/dashboard"),
      15000
    );

    const url = await driver.getCurrentUrl();

    assert.ok(url.includes("/dashboard"));
  });
});