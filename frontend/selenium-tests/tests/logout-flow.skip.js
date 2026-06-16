const { Builder, By, until } = require("selenium-webdriver");
require("chromedriver");
const assert = require("assert");

describe("KRINTERIOR Logout Flow", function () {
  this.timeout(60000);

  let driver;

  before(async () => {
    driver = await new Builder().forBrowser("chrome").build();
  });

  after(async () => {
    await driver.quit();
  });

  it("should login and logout successfully", async () => {

    // Open login page
    await driver.get("http://localhost:3000/login");

    // Login
    await driver.findElement(
      By.css('[data-testid="email-input"]')
    ).sendKeys("rev@example.com");

    await driver.findElement(
      By.css('[data-testid="password-input"]')
    ).sendKeys("123456");

    await driver.findElement(
      By.css('[data-testid="login-submit-btn"]')
    ).click();

    // Wait for dashboard
    await driver.wait(
      until.urlContains("/dashboard"),
      15000
    );

    console.log("✅ Login successful");

    // Wait for logout button
    await driver.wait(
      until.elementLocated(
        By.css('[data-testid="nav-logout"]')
      ),
      10000
    );

    // Click logout
    await driver.findElement(
      By.css('[data-testid="nav-logout"]')
    ).click();

    // Give React Router time
    await driver.sleep(3000);

    const url = await driver.getCurrentUrl();

    console.log("Logout URL:", url);

    assert.ok(
      url.includes("/login") ||
      url === "http://localhost:3000/" ||
      url === "http://localhost:3000"
    );

    console.log("✅ Logout successful");
  });
});