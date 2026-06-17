const fs = require("fs");
const path = require("path");
const { Builder, until } = require("selenium-webdriver");
const chrome = require("selenium-webdriver/chrome");

const BASE_URL = process.env.APP_BASE_URL || "http://localhost:3000";

async function createDriver() {
  const options = new chrome.Options();
  options.addArguments("--headless=new");
  options.addArguments("--no-sandbox");
  options.addArguments("--disable-dev-shm-usage");
  options.addArguments("--disable-gpu");
  options.addArguments("--window-size=1440,1000");
  if (process.env.CHROME_BIN) {
    options.setChromeBinaryPath(process.env.CHROME_BIN);
  }

  let builder = new Builder()
    .forBrowser("chrome")
    .setChromeOptions(options);

  if (process.env.CHROMEDRIVER_BIN) {
    const serviceBuilder = new chrome.ServiceBuilder(process.env.CHROMEDRIVER_BIN);
    builder = builder.setChromeService(serviceBuilder);
  }

  return builder.build();
}

async function openPath(driver, path) {
  await driver.get(`${BASE_URL}${path}`);
}

async function find(driver, locator, timeout = 15000) {
  const element = await driver.wait(until.elementLocated(locator), timeout);
  await driver.wait(until.elementIsVisible(element), timeout);
  return element;
}

async function safeClick(driver, locatorOrElement, timeout = 15000) {
  const element =
    typeof locatorOrElement.findElements === "function"
      ? locatorOrElement
      : await find(driver, locatorOrElement, timeout);
  await driver.executeScript("arguments[0].scrollIntoView({block:'center', inline:'center'});", element);
  await driver.wait(until.elementIsEnabled(element), timeout);
  await driver.executeScript("arguments[0].click();", element);
}

async function typeInto(driver, locator, value, timeout = 15000) {
  const element = await find(driver, locator, timeout);
  await element.clear();
  await element.sendKeys(value);
  return element;
}

async function captureScreenshot(driver, name) {
  const screenshotsDir = path.resolve(process.cwd(), "screenshots");
  fs.mkdirSync(screenshotsDir, { recursive: true });
  const filePath = path.join(screenshotsDir, `${name}-${Date.now()}.png`);
  const base64 = await driver.takeScreenshot();
  fs.writeFileSync(filePath, base64, "base64");
  return filePath;
}

module.exports = {
  BASE_URL,
  captureScreenshot,
  createDriver,
  find,
  openPath,
  safeClick,
  typeInto,
  until,
};
