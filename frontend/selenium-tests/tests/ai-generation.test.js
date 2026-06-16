const { Builder, By, until } = require("selenium-webdriver");
require("chromedriver");
const path = require("path");
const assert = require("assert");

describe("KRINTERIOR AI Generation Test", function () {
  this.timeout(300000); // 5 minutes

  let driver;

  before(async () => {
    driver = await new Builder().forBrowser("chrome").build();
  });

  after(async () => {
    await driver.quit();
  });

  // Helper function for clicking elements safely
  async function safeClick(element) {
    await driver.executeScript(
      "arguments[0].scrollIntoView({block:'center'});",
      element
    );
    await driver.sleep(500);

    await driver.executeScript(
      "arguments[0].click();",
      element
    );
  }

  it("should generate an AI interior design", async () => {

    // ======================
    // LOGIN
    // ======================
    await driver.get("http://localhost:3000/login");

    await driver.wait(
      until.elementLocated(
        By.css('[data-testid="email-input"]')
      ),
      10000
    );

    await driver.findElement(
      By.css('[data-testid="email-input"]')
    ).sendKeys("rev@example.com");

    await driver.findElement(
      By.css('[data-testid="password-input"]')
    ).sendKeys("123456");

    await driver.findElement(
      By.css('[data-testid="login-submit-btn"]')
    ).click();

    await driver.wait(
      until.urlContains("/dashboard"),
      15000
    );

    console.log("✅ Login successful");

    // ======================
    // OPEN CREATE PAGE
    // ======================
    await driver.get("http://localhost:3000/create");

    await driver.wait(
      until.elementLocated(
        By.css('[data-testid="upload-dropzone"]')
      ),
      10000
    );

    console.log("✅ Create page loaded");

    // ======================
    // UPLOAD IMAGE
    // ======================
    const upload = await driver.findElement(
      By.css('[data-testid="upload-input"]')
    );

    // Unhide hidden input
    await driver.executeScript(
      "arguments[0].style.display='block';",
      upload
    );

    const imagePath = path.resolve(
      __dirname,
      "../assets/before.jpg"
    );

    console.log("Uploading:", imagePath);

    await upload.sendKeys(imagePath);

    // Wait for image preview
    await driver.wait(
      until.elementLocated(
        By.css('[data-testid="upload-clear-btn"]')
      ),
      15000
    );

    console.log("✅ Image uploaded");

    // ======================
    // NEXT TO ROOM TYPE
    // ======================
await driver.sleep(3000);

const nextBtn = await driver.findElement(
  By.css('[data-testid="wizard-next-btn"]')
);

await safeClick(nextBtn);

console.log("Clicked Next");

await driver.sleep(3000);

const url = await driver.getCurrentUrl();
console.log("Current URL:", url);

const rooms = await driver.findElements(
  By.css('[data-testid^="room-"]')
);

console.log("Rooms found:", rooms.length);

const body = await driver.findElement(
  By.tagName("body")
).getText();

console.log(body.substring(0, 1000));

if (rooms.length === 0) {
  throw new Error("Room cards not found");
}

const room = rooms[0];

await safeClick(room);

console.log("✅ Room selected");

await driver.sleep(2000);

const nextBtn2 = await driver.findElement(
  By.css('[data-testid="wizard-next-btn"]')
);

await safeClick(nextBtn2);

await driver.sleep(3000);

    // ======================
    // BUDGET
    // ======================
    await driver.wait(
      until.elementLocated(
        By.css('[data-testid="budget-200000"]')
      ),
      20000
    );

    const budget = await driver.findElement(
      By.css('[data-testid="budget-200000"]')
    );

await safeClick(budget);

console.log("✅ Budget selected");

await driver.sleep(2000);

const nextBtn3 = await driver.findElement(
  By.css('[data-testid="wizard-next-btn"]')
);

await safeClick(nextBtn3);

await driver.sleep(3000);

    // ======================
    // PALETTE
    // ======================
    await driver.wait(
      until.elementLocated(
        By.css('[data-testid^="palette-"]')
      ),
      10000
    );

    const palette = await driver.findElement(
  By.css('[data-testid^="palette-"]')
);

await safeClick(palette);

console.log("✅ Palette selected");

await driver.sleep(2000);

const nextBtn4 = await driver.findElement(
  By.css('[data-testid="wizard-next-btn"]')
);

await safeClick(nextBtn4);

await driver.sleep(3000);

    // ======================
    // REQUIREMENTS
    // ======================
    await driver.wait(
      until.elementLocated(
        By.css('[data-testid="requirements-input"]')
      ),
      10000
    );

    await driver.findElement(
      By.css('[data-testid="requirements-input"]')
    ).sendKeys(
      "Modern luxury interior with warm lighting"
    );

    console.log("✅ Requirements entered");

    // ======================
    // GENERATE
    // ======================
    const generateBtn = await driver.findElement(
      By.css('[data-testid="wizard-generate-btn"]')
    );

    await safeClick(generateBtn);

    console.log("⏳ Waiting for AI generation...");

    // Wait for result page
    await driver.wait(
      until.urlContains("/result"),
      180000 // 3 minutes
    );

    console.log("✅ Result page opened");

    // ======================
    // VERIFY RESULT
    // ======================
    await driver.wait(
      until.elementLocated(
        By.css('[data-testid="before-after"]')
      ),
      30000
    );

    const result = await driver.findElement(
      By.css('[data-testid="before-after"]')
    );

    assert.ok(result);

    console.log("🎉 AI generation successful!");
  });
});