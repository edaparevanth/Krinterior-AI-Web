const { By } = require("selenium-webdriver");
const assert = require("assert");
const { createDriver, openPath, safeClick, typeInto, until } = require("../helpers/driver");

describe("KRINTERIOR Logout Flow", function () {
  this.timeout(60000);
  let driver;

  before(async () => {
    driver = await createDriver();
  });

  after(async () => {
    if (driver) await driver.quit();
  });

  it("should logout successfully", async () => {
    await openPath(driver, "/login");
    await typeInto(driver, By.css('[data-testid="email-input"]'), "rev@example.com");
    await typeInto(driver, By.css('[data-testid="password-input"]'), "123456");
    await safeClick(driver, By.css('[data-testid="login-submit-btn"]'));
    await driver.wait(until.urlContains("/dashboard"), 15000);

    await safeClick(driver, By.css('[data-testid="nav-logout"]'));
    await driver.wait(until.urlIs(`${process.env.APP_BASE_URL || "http://localhost:3000"}/`), 15000);
    const url = await driver.getCurrentUrl();

    assert.ok(url.endsWith("/"));
  });
});
