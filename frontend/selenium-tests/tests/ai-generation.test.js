const { By } = require("selenium-webdriver");
const path = require("path");
const assert = require("assert");
const { createDriver, find, openPath, safeClick, typeInto, until } = require("../helpers/driver");

describe("KRINTERIOR AI Generation Test", function () {
  this.timeout(180000);
  let driver;

  before(async () => {
    driver = await createDriver();
  });

  after(async () => {
    if (driver) await driver.quit();
  });

  it("should generate an AI interior design", async () => {
    await openPath(driver, "/login");
    await typeInto(driver, By.css('[data-testid="email-input"]'), "rev@example.com");
    await typeInto(driver, By.css('[data-testid="password-input"]'), "123456");
    await safeClick(driver, By.css('[data-testid="login-submit-btn"]'));
    await driver.wait(until.urlContains("/dashboard"), 15000);

    await openPath(driver, "/create");
    await find(driver, By.css('[data-testid="upload-dropzone"]'));

    const upload = await find(driver, By.css('[data-testid="upload-input"]'));
    await driver.executeScript("arguments[0].style.display='block';", upload);
    await upload.sendKeys(path.resolve(__dirname, "../assets/before.jpg"));
    await find(driver, By.css('[data-testid="upload-clear-btn"]'));

    await safeClick(driver, By.css('[data-testid="wizard-next-btn"]'));
    const room = await find(driver, By.css('[data-testid^="room-"]'));
    await safeClick(driver, room);

    await safeClick(driver, By.css('[data-testid="wizard-next-btn"]'));
    await safeClick(driver, By.css('[data-testid="budget-200000"]'));

    await safeClick(driver, By.css('[data-testid="wizard-next-btn"]'));
    const palette = await find(driver, By.css('[data-testid^="palette-"]'));
    await safeClick(driver, palette);

    await safeClick(driver, By.css('[data-testid="wizard-next-btn"]'));
    await typeInto(driver, By.css('[data-testid="requirements-input"]'), "Modern luxury interior with warm lighting");
    await safeClick(driver, By.css('[data-testid="wizard-generate-btn"]'));

    await driver.wait(until.urlContains("/result"), 30000);
    const result = await find(driver, By.css('[data-testid="before-after"]'), 30000);

    assert.ok(result);
  });
});
