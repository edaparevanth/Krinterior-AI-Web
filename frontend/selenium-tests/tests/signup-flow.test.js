const { By } = require("selenium-webdriver");
const assert = require("assert");
const { createDriver, openPath, safeClick, typeInto, until } = require("../helpers/driver");

describe("KRINTERIOR Signup Flow", function () {
  this.timeout(60000);
  let driver;

  before(async () => {
    driver = await createDriver();
  });

  after(async () => {
    if (driver) await driver.quit();
  });

  it("should signup successfully", async () => {
    const uniqueEmail = `test${Date.now()}@gmail.com`;

    await openPath(driver, "/signup");
    await typeInto(driver, By.css('[data-testid="name-input"]'), "Selenium Test");
    await typeInto(driver, By.css('[data-testid="signup-email-input"]'), uniqueEmail);
    await typeInto(driver, By.css('[data-testid="signup-password-input"]'), "password123");
    await safeClick(driver, By.css('[data-testid="signup-submit-btn"]'));

    await driver.wait(until.urlContains("/dashboard"), 15000);
    const url = await driver.getCurrentUrl();

    assert.ok(url.includes("/dashboard"));
  });
});
