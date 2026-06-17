const { By } = require("selenium-webdriver");
const assert = require("assert");
const { captureScreenshot, createDriver, openPath, safeClick, typeInto, until } = require("../helpers/driver");

describe("KRINTERIOR Logout Flow", function () {
  this.timeout(90000);
  let driver;

  before(async () => {
    driver = await createDriver();
  });

  after(async () => {
    if (driver) await driver.quit();
  });

  it("should logout successfully", async () => {
    try {
      await openPath(driver, "/login");
      await typeInto(driver, By.css('[data-testid="email-input"]'), "rev@example.com");
      await typeInto(driver, By.css('[data-testid="password-input"]'), "123456");
      await safeClick(driver, By.css('[data-testid="login-submit-btn"]'));
      await driver.wait(until.urlContains("/dashboard"), 15000);

      await safeClick(driver, By.css('[data-testid="nav-logout"]'));
      await driver.wait(
        async () => {
          const currentUrl = await driver.getCurrentUrl();
          return currentUrl.includes("3000") && !currentUrl.includes("/dashboard");
        },
        30000
      );

      const url = await driver.getCurrentUrl();
      assert.ok(url.includes("3000"), `Expected logout redirect to include 3000, got: ${url}`);
      assert.ok(!url.includes("/dashboard"), `Logout should leave dashboard, got: ${url}`);
    } catch (error) {
      await captureScreenshot(driver, "logout-flow-failure");
      throw error;
    }
  });
});
