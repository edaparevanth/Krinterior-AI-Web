const { By } = require("selenium-webdriver");
const assert = require("assert");
const { createDriver, find, openPath } = require("../helpers/driver");

describe("KRINTERIOR Login Page Test", function () {
  this.timeout(60000);
  let driver;

  before(async () => {
    driver = await createDriver();
  });

  after(async () => {
    if (driver) await driver.quit();
  });

  it("should open login page and find form fields", async () => {
    await openPath(driver, "/login");

    const email = await find(driver, By.css('[data-testid="email-input"]'));
    const password = await find(driver, By.css('[data-testid="password-input"]'));
    const button = await find(driver, By.css('[data-testid="login-submit-btn"]'));

    assert.ok(email);
    assert.ok(password);
    assert.ok(button);
  });
});
