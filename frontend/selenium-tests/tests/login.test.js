const { Builder, By, until } = require("selenium-webdriver");
require("chromedriver");
const assert = require("assert");

describe("KRINTERIOR Login Page Test", function () {
  this.timeout(30000);

  let driver;

  before(async () => {
    driver = await new Builder().forBrowser("chrome").build();
  });

  after(async () => {
    await driver.quit();
  });

  it("should open login page and find form fields", async () => {
    await driver.get("http://localhost:3000/login");

    await driver.wait(
      until.elementLocated(By.css('[data-testid="email-input"]')),
      10000
    );

    const email = await driver.findElement(
      By.css('[data-testid="email-input"]')
    );

    const password = await driver.findElement(
      By.css('[data-testid="password-input"]')
    );

    const button = await driver.findElement(
      By.css('[data-testid="login-submit-btn"]')
    );

    assert.ok(email);
    assert.ok(password);
    assert.ok(button);
  });
});