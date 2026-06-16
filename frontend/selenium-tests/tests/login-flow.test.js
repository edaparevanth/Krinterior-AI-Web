const { Builder, By, until } = require("selenium-webdriver");
require("chromedriver");
const assert = require("assert");

describe("KRINTERIOR Login Flow", function () {
  this.timeout(60000);

  let driver;

  before(async () => {
    driver = await new Builder().forBrowser("chrome").build();
  });

  after(async () => {
    await driver.quit();
  });

  it("should login successfully", async () => {
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

    const loginBtn = await driver.findElement(
      By.css('[data-testid="login-submit-btn"]')
    );

    // Replace with your test account
    await email.sendKeys("rev@example.com");
    await password.sendKeys("123456");

    await loginBtn.click();

    // Wait for dashboard URL
    await driver.wait(until.urlContains("/dashboard"), 15000);

    const url = await driver.getCurrentUrl();

    assert.ok(url.includes("/dashboard"));
  });
});