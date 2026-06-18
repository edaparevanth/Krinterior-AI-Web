# Krinterior AI - 200 E2E Test Cases Database
# 100 Selenium (Web) and 100 Appium (Mobile) test cases

TEST_CASES = [
    # ==========================================
    # SELENIUM WEB TEST CASES (TC001 - TC100)
    # ==========================================
    {
        "id": "TC001",
        "tool": "Selenium",
        "category": "Landing & Navigation",
        "title": "Verify Landing Page Title and Meta Headers",
        "description": "Ensure that the landing page has correct SEO titles and meta descriptions loaded.",
        "steps": "1. Open browser\n2. Navigate to root URL\n3. Verify page title contains 'Krinterior AI'\n4. Verify meta description presence.",
        "expected": "Title matches 'Krinterior AI' and SEO tags are present."
    },
    {
        "id": "TC002",
        "tool": "Selenium",
        "category": "Landing & Navigation",
        "title": "Verify Navigation Bar Links",
        "description": "Check if nav items (Home, Features, Pricing, Login, Signup) are visible and clickable.",
        "steps": "1. Navigate to Landing Page\n2. Inspect navbar links\n3. Click Features link\n4. Verify scrolling or redirection.",
        "expected": "All navigation options are visible, clickable, and direct to correct sections."
    },
    {
        "id": "TC003",
        "tool": "Selenium",
        "category": "Landing & Navigation",
        "title": "Verify Call to Action (CTA) Button on Hero Section",
        "description": "Verify 'Get Started' button redirects the user to the signup or login page.",
        "steps": "1. Go to Landing Page\n2. Locate 'Get Started' CTA\n3. Click the CTA\n4. Verify target URL.",
        "expected": "User is redirected to the `/signup` page."
    },
    {
        "id": "TC004",
        "tool": "Selenium",
        "category": "Landing & Navigation",
        "title": "Verify Smooth Scrolling to Sections",
        "description": "Test if clicking sections in landing nav smooth-scrolls to target element IDs.",
        "steps": "1. Load landing page\n2. Click 'How it Works'\n3. Verify page viewport scroll offset changed.",
        "expected": "Viewport scrolls smoothly to the 'How it Works' block."
    },
    {
        "id": "TC005",
        "tool": "Selenium",
        "category": "Landing & Navigation",
        "title": "Verify Footer Links and Copyright Notice",
        "description": "Verify footer holds social, terms, and privacy policy links along with correct year.",
        "steps": "1. Scroll to the bottom of Landing page\n2. Check links structure\n3. Verify copyright text contains active year.",
        "expected": "All links are intact and year matches current system time."
    },
    {
        "id": "TC006",
        "tool": "Selenium",
        "category": "Landing & Navigation",
        "title": "Verify Pricing Toggle Functionality",
        "description": "Test switching between monthly and annual plans on landing page.",
        "steps": "1. Go to Pricing section\n2. Click 'Annual Billing' toggle\n3. Verify pricing numbers update.",
        "expected": "Prices update to show discounted annual rates."
    },
    {
        "id": "TC007",
        "tool": "Selenium",
        "category": "Landing & Navigation",
        "title": "Verify Logo Redirects to Landing Page",
        "description": "Ensure clicking the brand logo on any route redirects back to home.",
        "steps": "1. Navigate to a subpage (e.g. `/login`)\n2. Click the brand logo\n3. Verify URL.",
        "expected": "User returns to `/` path."
    },
    {
        "id": "TC008",
        "tool": "Selenium",
        "category": "Landing & Navigation",
        "title": "Verify Testimonial Card Display",
        "description": "Ensure client reviews are visible with user avatars and text.",
        "steps": "1. Scroll to testimonials section\n2. Verify client cards are present.",
        "expected": "Review cards show rating stars, feedback text, and names."
    },
    {
        "id": "TC009",
        "tool": "Selenium",
        "category": "Landing & Navigation",
        "title": "Verify FAQ Section Accordion Behavior",
        "description": "Verify clicking FAQ question expands corresponding answer.",
        "steps": "1. Scroll to FAQs\n2. Click a question card\n3. Verify answer display state changes.",
        "expected": "Answer expands down smoothly; other answers stay collapsed."
    },
    {
        "id": "TC010",
        "tool": "Selenium",
        "category": "Landing & Navigation",
        "title": "Verify Contact Us Form Input Validation",
        "description": "Ensure empty submit triggers warning indicators.",
        "steps": "1. Scroll to Contact form\n2. Leave fields blank and click 'Send'\n3. Observe message.",
        "expected": "Validation error appears for Name, Email, and Message fields."
    },
    {
        "id": "TC011",
        "tool": "Selenium",
        "category": "Landing & Navigation",
        "title": "Verify Contact Us Success Submission",
        "description": "Submit contact form with correct inputs.",
        "steps": "1. Enter valid email, name, message\n2. Click Send\n3. Verify success indicator.",
        "expected": "Shows 'Thank you for contacting us' toast or alert."
    },
    {
        "id": "TC012",
        "tool": "Selenium",
        "category": "Landing & Navigation",
        "title": "Verify Features List Hover Effects",
        "description": "Check styling response when hovering over feature highlight items.",
        "steps": "1. Hover mouse over AI rendering feature icon\n2. Observe border and background style change.",
        "expected": "Shadow depth and color change smoothly on hover."
    },
    {
        "id": "TC013",
        "tool": "Selenium",
        "category": "Landing & Navigation",
        "title": "Verify Newsletter Subscription Email validation",
        "description": "Test entering incorrect format in newsletter footer input.",
        "steps": "1. Enter 'abc' in subscription field\n2. Press Enter\n3. Observe validation toast.",
        "expected": "Shows email format validation warning."
    },
    {
        "id": "TC014",
        "tool": "Selenium",
        "category": "Landing & Navigation",
        "title": "Verify Newsletter Subscription Success",
        "description": "Submit correct email for subscription.",
        "steps": "1. Enter 'valid@example.com'\n2. Click Subscribe\n3. Verify confirmation toaster.",
        "expected": "Success toast 'Subscribed successfully!' is shown."
    },
    {
        "id": "TC015",
        "tool": "Selenium",
        "category": "Landing & Navigation",
        "title": "Verify Client Logotypes Banner",
        "description": "Verify external developer / client brand logos display in hero strip.",
        "steps": "1. View bottom of Hero section\n2. Verify brand logos are visible.",
        "expected": "Partners/Clients banner is loaded correctly."
    },
    {
        "id": "TC016",
        "tool": "Selenium",
        "category": "User Authentication",
        "title": "Successful Signup with valid credentials",
        "description": "Verify a new user can sign up using email and password.",
        "steps": "1. Go to `/signup`\n2. Input new email, name, and password\n3. Click 'Sign Up'\n4. Verify dashboard load.",
        "expected": "Successfully signs up, redirects to `/dashboard`, and creates user session."
    },
    {
        "id": "TC017",
        "tool": "Selenium",
        "category": "User Authentication",
        "title": "Signup Validation for existing email",
        "description": "Verify that signing up with an already registered email throws an error.",
        "steps": "1. Go to `/signup`\n2. Enter existing email and credentials\n3. Submit\n4. Observe error message.",
        "expected": "Validation message 'Email already exists' is displayed."
    },
    {
        "id": "TC018",
        "tool": "Selenium",
        "category": "User Authentication",
        "title": "Signup Password Strength Enforcement",
        "description": "Ensure weak passwords (e.g., short, no numbers) trigger validations.",
        "steps": "1. Go to `/signup`\n2. Fill valid email, name\n3. Enter password '123'\n4. Check for validation indicator.",
        "expected": "UI prevents submission and states password must be at least 6 characters."
    },
    {
        "id": "TC019",
        "tool": "Selenium",
        "category": "User Authentication",
        "title": "Successful Email Login",
        "description": "Verify registered user can log in successfully.",
        "steps": "1. Navigate to `/login`\n2. Fill registered email and password\n3. Click 'Login'\n4. Verify redirect.",
        "expected": "Redirects to `/dashboard` with session token cookie set."
    },
    {
        "id": "TC020",
        "tool": "Selenium",
        "category": "User Authentication",
        "title": "Login validation on wrong password",
        "description": "Verify error message when logging in with invalid password.",
        "steps": "1. Navigate to `/login`\n2. Enter valid email, wrong password\n3. Click Login\n4. Verify error toaster.",
        "expected": "Shows error 'Invalid email or password' or status 401."
    },
    {
        "id": "TC021",
        "tool": "Selenium",
        "category": "User Authentication",
        "title": "Login validation on unformatted email",
        "description": "Check if front-end validates malformed email entries.",
        "steps": "1. Go to `/login`\n2. Type 'testuser.com' in email field\n3. Type password\n4. Observe browser or form validation.",
        "expected": "Displays 'Please enter a valid email address'."
    },
    {
        "id": "TC022",
        "tool": "Selenium",
        "category": "User Authentication",
        "title": "Verify Google OAuth Link",
        "description": "Ensure clicking Google login redirects to authentication provider.",
        "steps": "1. Go to `/login`\n2. Click 'Continue with Google' button\n3. Verify OAuth provider landing page is loaded.",
        "expected": "Redirected to Google accounts/oauth login page."
    },
    {
        "id": "TC023",
        "tool": "Selenium",
        "category": "User Authentication",
        "title": "Verify OAuth callback handling",
        "description": "Test that returning from OAuth with session token sets cookies.",
        "steps": "1. Navigate directly to `/auth/callback#session_id=test-token`\n2. Observe route change and authentication context initialization.",
        "expected": "Session cookies are set and client auto-navigates to `/dashboard`."
    },
    {
        "id": "TC024",
        "tool": "Selenium",
        "category": "User Authentication",
        "title": "Unauthenticated user route redirection",
        "description": "Ensure protected routes redirect anonymous users to login.",
        "steps": "1. Clear browser cookies\n2. Try to access `/dashboard` or `/create` directly\n3. Observe redirection.",
        "expected": "Page automatically redirects to `/login`."
    },
    {
        "id": "TC025",
        "tool": "Selenium",
        "category": "User Authentication",
        "title": "Logout Action",
        "description": "Verify clicking logout clears sessions and redirects to landing page.",
        "steps": "1. Login successfully\n2. Click Profile -> Logout\n3. Verify cookies cleared\n4. Verify redirect to landing page.",
        "expected": "Cookies are removed and user lands back on `/`."
    },
    {
        "id": "TC026",
        "tool": "Selenium",
        "category": "User Authentication",
        "title": "Verify Session Token Persistence on Refresh",
        "description": "Ensure user remains logged in after hard browser reload.",
        "steps": "1. Login\n2. Reload page via driver.refresh()\n3. Verify dashboard remains loaded.",
        "expected": "Dashboard doesn't redirect to login; session cookie is preserved."
    },
    {
        "id": "TC027",
        "tool": "Selenium",
        "category": "User Authentication",
        "title": "Verify Password Visibility Toggle",
        "description": "Check if clicking the eye icon toggles password input type (text/password).",
        "steps": "1. Go to `/login`\n2. Type into password field\n3. Click eye icon\n4. Verify input tag type attribute.",
        "expected": "Input type switches to 'text' showing password, then back to 'password'."
    },
    {
        "id": "TC028",
        "tool": "Selenium",
        "category": "User Authentication",
        "title": "Verify Forgot Password Form Redirection",
        "description": "Ensure clicking 'Forgot Password' link navigates to recovery page.",
        "steps": "1. Go to `/login`\n2. Click 'Forgot password?' link\n3. Verify URL.",
        "expected": "Navigates to password recovery routing endpoint."
    },
    {
        "id": "TC029",
        "tool": "Selenium",
        "category": "User Authentication",
        "title": "Verify Reset Password Request Submission",
        "description": "Test submitting password recovery request form.",
        "steps": "1. On recovery page, enter email\n2. Click 'Send Reset Link'\n3. Verify notification message.",
        "expected": "Shows confirmation toast 'Password reset email sent'."
    },
    {
        "id": "TC030",
        "tool": "Selenium",
        "category": "User Authentication",
        "title": "Verify OAuth Token Refresh",
        "description": "Verify that backend refresh endpoint correctly restores session tokens.",
        "steps": "1. Login with session token close to expiry\n2. Execute API check\n3. Verify session updates.",
        "expected": "User is issued new session token automatically."
    },
    {
        "id": "TC031",
        "tool": "Selenium",
        "category": "User Authentication",
        "title": "Verify User Sign Up Terms Checkbox",
        "description": "Verify terms and conditions checkbox validation.",
        "steps": "1. Fill signup inputs\n2. Leave 'Agree to terms' checkbox unchecked\n3. Click Sign Up.",
        "expected": "UI blocks submission and displays 'You must agree to terms'."
    },
    {
        "id": "TC032",
        "tool": "Selenium",
        "category": "User Authentication",
        "title": "Verify Signup input trims white space",
        "description": "Ensure spaces in signup email input are trimmed before API request.",
        "steps": "1. Type ' emailwithspaces@test.com ' in email field\n2. Register\n3. Inspect registration database record.",
        "expected": "Email is registered as 'emailwithspaces@test.com' without whitespace."
    },
    {
        "id": "TC033",
        "tool": "Selenium",
        "category": "User Authentication",
        "title": "Verify Login input trims white space",
        "description": "Ensure spaces in login email input are trimmed before processing.",
        "steps": "1. Type ' emailwithspaces@test.com ' in email login field\n2. Submit credentials.",
        "expected": "Login completes successfully."
    },
    {
        "id": "TC034",
        "tool": "Selenium",
        "category": "User Authentication",
        "title": "Verify Login Rate Limiter Protection",
        "description": "Ensure 5 quick consecutive failed logins trigger lockout.",
        "steps": "1. Enter wrong credentials 5 times rapidly\n2. Attempt 6th login\n3. Inspect error state.",
        "expected": "Error message displays 'Too many attempts, try again later'."
    },
    {
        "id": "TC035",
        "tool": "Selenium",
        "category": "User Authentication",
        "title": "Verify Multi-tab Session Sync",
        "description": "Logging out in one tab should log out the user in secondary tabs.",
        "steps": "1. Open two tabs on `/dashboard`\n2. Log out in tab 1\n3. Focus tab 2 and perform action.",
        "expected": "Tab 2 automatically redirects to `/login`."
    },
    {
        "id": "TC036",
        "tool": "Selenium",
        "category": "User Dashboard",
        "title": "Verify Dashboard Greeting and User Profile Info",
        "description": "Verify user name is shown correctly in the dashboard header.",
        "steps": "1. Login with Test User credentials\n2. Check greeting text in top-right or sidebar\n3. Compare with registered database name.",
        "expected": "Displays 'Welcome, Test User' or equivalent correct name."
    },
    {
        "id": "TC037",
        "tool": "Selenium",
        "category": "User Dashboard",
        "title": "Check Empty State on New User Dashboard",
        "description": "Verify that new users see an instructions prompt and 'Create Project' call-to-action.",
        "steps": "1. Signup new user\n2. Land on dashboard\n3. Verify project grid displays 'No projects found yet'.",
        "expected": "Dashboard empty state contains a 'Generate Design' button."
    },
    {
        "id": "TC038",
        "tool": "Selenium",
        "category": "User Dashboard",
        "title": "Verify Create Project CTA on Dashboard",
        "description": "Verify the main floating/header button redirects to create wizard.",
        "steps": "1. Load dashboard\n2. Click 'New Design' / 'Create Project'\n3. Verify navigation route.",
        "expected": "User is successfully navigated to `/create`."
    },
    {
        "id": "TC039",
        "tool": "Selenium",
        "category": "User Dashboard",
        "title": "Verify Navigation Sidebar Toggle",
        "description": "Verify collapsible sidebar navigation functions correctly.",
        "steps": "1. Load dashboard\n2. Click sidebar toggle button\n3. Observe sidebar width change and menu labels behavior.",
        "expected": "Sidebar collapses to compact icon view and expands cleanly."
    },
    {
        "id": "TC040",
        "tool": "Selenium",
        "category": "User Dashboard",
        "title": "Verify Quick Stats Cards Count",
        "description": "Verify active project count, vastu compliance count match API data.",
        "steps": "1. Load dashboard\n2. Check counts in top stats grid\n3. Compare with project items list count.",
        "expected": "Active project count and total designs match the actual listing count."
    },
    {
        "id": "TC041",
        "tool": "Selenium",
        "category": "User Dashboard",
        "title": "Verify Quick Access to Recent Project",
        "description": "Ensure clicking the first project card opens it quickly.",
        "steps": "1. Load dashboard with existing projects\n2. Click the top-most project card\n3. Verify URL changes to `/project/:id`.",
        "expected": "User details view is successfully loaded."
    },
    {
        "id": "TC042",
        "tool": "Selenium",
        "category": "User Dashboard",
        "title": "Verify Theme Switcher: Dark/Light Mode",
        "description": "Check if dashboard updates color scheme when theme switcher is toggled.",
        "steps": "1. Click Dark Mode toggle icon in dashboard header\n2. Check `html` tags for dark mode classes.",
        "expected": "Theme changes and styles switch accordingly."
    },
    {
        "id": "TC043",
        "tool": "Selenium",
        "category": "User Dashboard",
        "title": "Verify User Profile Avatar Upload",
        "description": "Ensure user can upload a custom profile avatar photo.",
        "steps": "1. Navigate to Settings page\n2. Click Profile Image -> Upload\n3. Select avatar.png\n4. Confirm upload.",
        "expected": "Avatar thumbnail updates in header nav."
    },
    {
        "id": "TC044",
        "tool": "Selenium",
        "category": "User Dashboard",
        "title": "Verify Profile Name Edit Save",
        "description": "Verify changing profile name updates state correctly.",
        "steps": "1. Go to profile settings\n2. Change name from 'Test User' to 'User 2'\n3. Save details\n4. Observe dashboard greeting.",
        "expected": "Greeting changes to 'Welcome, User 2'."
    },
    {
        "id": "TC045",
        "tool": "Selenium",
        "category": "User Dashboard",
        "title": "Verify Email Settings Notification Toggles",
        "description": "Verify toggling dashboard email preferences saves settings.",
        "steps": "1. Go to notification settings\n2. Switch off 'Marketing Emails'\n3. Save changes\n4. Reload and check state.",
        "expected": "Marketing email preference remains toggled OFF."
    },
    {
        "id": "TC046",
        "tool": "Selenium",
        "category": "User Dashboard",
        "title": "Verify Upgrade Account subscription checkout link",
        "description": "Verify 'Go Premium' link points to checkout integration page.",
        "steps": "1. Click 'Go Premium' button\n2. Verify redirect or modal details.",
        "expected": "Displays Premium checkout modal or billing details."
    },
    {
        "id": "TC047",
        "tool": "Selenium",
        "category": "User Dashboard",
        "title": "Verify Dashboard System Status Banner",
        "description": "Verify maintenance status banner doesn't show up unless flagged.",
        "steps": "1. Load dashboard\n2. Look for emergency/system notifications.",
        "expected": "Header banner is empty or hidden by default."
    },
    {
        "id": "TC048",
        "tool": "Selenium",
        "category": "User Dashboard",
        "title": "Verify Dashboard Sidebar links active highlight",
        "description": "Verify sidebar active tab styling updates when navigating.",
        "steps": "1. Navigate to Projects via sidebar\n2. Inspect CSS classes of sidebar link.",
        "expected": "Active project link receives border or background color highlight."
    },
    {
        "id": "TC049",
        "tool": "Selenium",
        "category": "User Dashboard",
        "title": "Verify Help & Support Modal Launcher",
        "description": "Ensure help button opens contact/support modal dialog.",
        "steps": "1. Click support widget button in bottom sidebar\n2. Verify popup display state.",
        "expected": "Help modal details are displayed with FAQ shortcuts."
    },
    {
        "id": "TC050",
        "tool": "Selenium",
        "category": "User Dashboard",
        "title": "Verify User Log History list loading",
        "description": "Verify account log history loads events properly.",
        "steps": "1. Go to Account Settings -> Activity Logs\n2. Check log listings presence.",
        "expected": "List shows login locations, times, and activities."
    },
    {
        "id": "TC051",
        "tool": "Selenium",
        "category": "Create Wizard",
        "title": "Wizard Step 1: Select Room Type",
        "description": "Verify room type selection highlights selected box and unlocks next step.",
        "steps": "1. Go to `/create`\n2. Click 'Living Room'\n3. Verify Next button is enabled.",
        "expected": "Living Room card shows active style border; Next button can be clicked."
    },
    {
        "id": "TC052",
        "tool": "Selenium",
        "category": "Create Wizard",
        "title": "Wizard Step 2: Select Theme Style",
        "description": "Verify style selections (Modern, Minimalist, Scandinavian, Vastu-compliant) operate correctly.",
        "steps": "1. Proceed to Wizard Step 2\n2. Select 'Modern'\n3. Click Next.",
        "expected": "Modern selection is recorded in internal form state."
    },
    {
        "id": "TC053",
        "tool": "Selenium",
        "category": "Create Wizard",
        "title": "Wizard Step 3: Input Budget Slider",
        "description": "Verify slider controls and numeric inputs update values reciprocally.",
        "steps": "1. Proceed to Wizard Step 3\n2. Move budget slider to $5000\n3. Verify input box displays 5000.",
        "expected": "Values are synchronized between slider and input text field."
    },
    {
        "id": "TC054",
        "tool": "Selenium",
        "category": "Create Wizard",
        "title": "Wizard Step 4: Add Room Dimensions",
        "description": "Validate inputs for length, width, and height.",
        "steps": "1. Proceed to Wizard Step 4\n2. Enter invalid inputs (negative numbers)\n3. Check validation error\n4. Enter valid dimensions (12x14x10 ft).",
        "expected": "Negative numbers trigger alert; positive dimensions enable next step."
    },
    {
        "id": "TC055",
        "tool": "Selenium",
        "category": "Create Wizard",
        "title": "Wizard Step 5: Vastu Shastra Toggles",
        "description": "Verify Vastu compliance options can be enabled/disabled.",
        "steps": "1. Proceed to Vastu step in wizard\n2. Toggle 'Enforce Vastu Principles' to ON\n3. Select entrance direction 'North-East'\n4. Click Next.",
        "expected": "Vastu preferences are successfully gathered in payload."
    },
    {
        "id": "TC056",
        "tool": "Selenium",
        "category": "Create Wizard",
        "title": "Wizard Step 6: File Upload - Room Image",
        "description": "Test upload button for blueprint or current room image.",
        "steps": "1. Go to upload section\n2. Select dummy PNG image file\n3. Verify progress indicator and upload preview.",
        "expected": "Image is uploaded and name/thumbnail appears in preview."
    },
    {
        "id": "TC057",
        "tool": "Selenium",
        "category": "Create Wizard",
        "title": "Wizard Back-Navigation State Retention",
        "description": "Verify backward button retains selections on previous steps.",
        "steps": "1. Go to Step 3 of the wizard\n2. Click 'Back' button\n3. Verify Step 2 theme selection is still active.",
        "expected": "Theme selection ('Modern') remains selected."
    },
    {
        "id": "TC058",
        "tool": "Selenium",
        "category": "Create Wizard",
        "title": "Wizard Form Incomplete Validation",
        "description": "Ensure user cannot bypass required fields to submit design request.",
        "steps": "1. Open `/create`\n2. Skip selections and try to trigger next step\n3. Verify system prevents proceeding.",
        "expected": "Validation errors appear; next button is disabled."
    },
    {
        "id": "TC059",
        "tool": "Selenium",
        "category": "Create Wizard",
        "title": "Wizard Multi-step Progress Bar Indicator",
        "description": "Verify that the active step indicator updates as you progress.",
        "steps": "1. Open `/create`\n2. Progress from Step 1 to Step 2\n3. Inspect stepper classes.",
        "expected": "Step 2 indicator changes status to 'active' or colored state."
    },
    {
        "id": "TC060",
        "tool": "Selenium",
        "category": "Create Wizard",
        "title": "Submit Design generation payload validation",
        "description": "Verify that payload sent to backend on submission holds all selected properties.",
        "steps": "1. Open DevTools or proxy logs\n2. Fill wizard fields and hit 'Submit'\n3. Inspect network request to `/api/design/generate`.",
        "expected": "JSON payload matches selections (room, style, budget, Vastu direction, uploaded file)."
    },
    {
        "id": "TC061",
        "tool": "Selenium",
        "category": "Create Wizard",
        "title": "Verify Multiple File Upload Handling",
        "description": "Ensure trying to upload more than the allowed limit (e.g. 5 files) displays warning.",
        "steps": "1. Select 6 image files for upload\n2. Submit\n3. Observe warning toast.",
        "expected": "UI restricts upload and displays limit validation."
    },
    {
        "id": "TC062",
        "tool": "Selenium",
        "category": "Create Wizard",
        "title": "Verify Unsupported File Type Upload Warning",
        "description": "Ensure PDF/TXT file upload in design image step gets rejected.",
        "steps": "1. Select text document file in dropzone\n2. Verify alert content.",
        "expected": "Error 'Invalid file format. Only JPG, PNG, and WebP are allowed' is displayed."
    },
    {
        "id": "TC063",
        "tool": "Selenium",
        "category": "Create Wizard",
        "title": "Verify File Upload Drag & Drop State styling",
        "description": "Verify dragover hover style on dropzone element.",
        "steps": "1. Drag local image over dropzone area\n2. Verify border changes to active dash lines.",
        "expected": "Dropzone border changes color/style indicating active drop state."
    },
    {
        "id": "TC064",
        "tool": "Selenium",
        "category": "Create Wizard",
        "title": "Verify Custom Requirements Text Limit",
        "description": "Verify textarea validator enforces character limits (e.g. 500 characters).",
        "steps": "1. Write 510 characters in custom requirements text area\n2. Verify character counter indicator status.",
        "expected": "Counter displays red colored text warning and cuts off input."
    },
    {
        "id": "TC065",
        "tool": "Selenium",
        "category": "Create Wizard",
        "title": "Verify Step 3 Preset Budgets Clicking",
        "description": "Ensure quick-preset budget options (Low, Medium, Premium) update form state.",
        "steps": "1. Navigate to Step 3\n2. Click 'Medium Budget' button card\n3. Check slider value.",
        "expected": "Slider value adjusts to corresponding preset amount."
    },
    {
        "id": "TC066",
        "tool": "Selenium",
        "category": "Create Wizard",
        "title": "Verify Dimension Unit Switcher (Ft to Meters)",
        "description": "Verify switching unit scales updates dimension values correctly.",
        "steps": "1. Enter '10' in Length field in feet\n2. Toggle units button to Meters\n3. Observe value.",
        "expected": "Value changes to corresponding conversion (e.g., ~3.05 meters)."
    },
    {
        "id": "TC067",
        "tool": "Selenium",
        "category": "Create Wizard",
        "title": "Verify Dimension Zero Value Input Validation",
        "description": "Ensure zero values are not allowed for dimensions.",
        "steps": "1. Enter 0 for Length/Width\n2. Click next\n3. Observe error details.",
        "expected": "Shows validation warning 'Dimensions must be greater than zero'."
    },
    {
        "id": "TC068",
        "tool": "Selenium",
        "category": "Create Wizard",
        "title": "Verify Floor Plan Template Choices",
        "description": "Check if preset floor plan template choices can be loaded.",
        "steps": "1. Go to Blueprint selection\n2. Click 'L-Shaped Room Template'\n3. Verify selection outline.",
        "expected": "Template outline selection border highlights successfully."
    },
    {
        "id": "TC069",
        "tool": "Selenium",
        "category": "Create Wizard",
        "title": "Verify Vastu Cardinal Direction Widget Toggle",
        "description": "Ensure direction quadrants can be toggled by keyboard arrows.",
        "steps": "1. Focus direction card\n2. Press right arrow on keyboard\n3. Check active state.",
        "expected": "Selection moves to next direction quadrant."
    },
    {
        "id": "TC070",
        "tool": "Selenium",
        "category": "Create Wizard",
        "title": "Verify Exit Wizard Warning Dialog",
        "description": "Verify exiting halfway prompts warning.",
        "steps": "1. Click close icon at top of wizard\n2. Verify warning modal displays.",
        "expected": "Warning modal asks user if they want to discard design details."
    },
    {
        "id": "TC071",
        "tool": "Selenium",
        "category": "Results & AI Generation",
        "title": "Verify AI Generation Loading State",
        "description": "Ensure loading screen shows micro-animations and helpful status updates.",
        "steps": "1. Submit wizard data\n2. Observe loading layout\n3. Check for animated spinner and status messages.",
        "expected": "Loading spinner spins; status messages ('Generating layouts...', 'Estimating budget...') update periodically."
    },
    {
        "id": "TC072",
        "tool": "Selenium",
        "category": "Results & AI Generation",
        "title": "Verify Generated Design Layout",
        "description": "Inspect that the generated design page correctly displays the AI-rendered image.",
        "steps": "1. Wait for generation completion\n2. Locate the main generated canvas/image element\n3. Verify image source is valid.",
        "expected": "AI design image is loaded from backend storage bucket."
    },
    {
        "id": "TC073",
        "tool": "Selenium",
        "category": "Results & AI Generation",
        "title": "Verify Budget Breakdown Table",
        "description": "Check if estimated costs/furniture list matches backend calculations.",
        "steps": "1. Navigate to `/result`\n2. Inspect 'Estimated Budget' segment\n3. Verify furniture items and prices are listed and total sum calculates correctly.",
        "expected": "List shows name, price, store links, and correct summary total."
    },
    {
        "id": "TC074",
        "tool": "Selenium",
        "category": "Results & AI Generation",
        "title": "Verify Vastu Compliance Score Card",
        "description": "Verify Vastu score badge and detailed advice text are shown.",
        "steps": "1. Navigate to design result page\n2. Verify presence of Vastu compliance meter/score\n3. Ensure advice details explain issues (e.g. bed placement).",
        "expected": "Vastu widget is populated with score (0-100) and actionable details."
    },
    {
        "id": "TC075",
        "tool": "Selenium",
        "category": "Results & AI Generation",
        "title": "Verify Save Project option",
        "description": "Verify that clicking 'Save Project' persists it to user's dashboard.",
        "steps": "1. Complete design generation\n2. Click 'Save to Projects'\n3. Observe confirmation notification\n4. Navigate to dashboard.",
        "expected": "Project appears in dashboard projects list."
    },
    {
        "id": "TC076",
        "tool": "Selenium",
        "category": "Results & AI Generation",
        "title": "Verify Export Design report to PDF",
        "description": "Verify that 'Export PDF' button works and triggers download.",
        "steps": "1. In results view, click 'Export PDF'\n2. Inspect browser downloads or mock window trigger.",
        "expected": "PDF file download is initiated."
    },
    {
        "id": "TC077",
        "tool": "Selenium",
        "category": "Results & AI Generation",
        "title": "Verify Regenerate Option",
        "description": "Verify that 'Regenerate' option allows user to query AI again with updated prompts.",
        "steps": "1. In results view, click 'Regenerate'\n2. Modify prompt\n3. Submit and verify new load.",
        "expected": "AI re-generates and displays revised layout version."
    },
    {
        "id": "TC078",
        "tool": "Selenium",
        "category": "Results & AI Generation",
        "title": "Verify Share Design link copy",
        "description": "Verify share button copies unique result URL to clipboard.",
        "steps": "1. Click 'Share Design' link\n2. Inspect clipboard text or toaster notice.",
        "expected": "Copied message appears; clipboard matches project detail path."
    },
    {
        "id": "TC079",
        "tool": "Selenium",
        "category": "Results & AI Generation",
        "title": "Verify Furniture Link Click Redirects",
        "description": "Verify clicking purchase link in budget table opens affiliate store page in new tab.",
        "steps": "1. Locate item link in budget breakdown table\n2. Click the link\n3. Verify new tab is opened with store URL.",
        "expected": "Store URL opens in new window segment."
    },
    {
        "id": "TC080",
        "tool": "Selenium",
        "category": "Results & AI Generation",
        "title": "Verify Color Palette swatches rendering",
        "description": "Verify colors suggested by AI render color swatch previews.",
        "steps": "1. Look at 'AI Suggested Colors' widget\n2. Verify hexagonal color values and visual colors match.",
        "expected": "Color cards contain appropriate hex codes and visual boxes."
    },
    {
        "id": "TC081",
        "tool": "Selenium",
        "category": "Results & AI Generation",
        "title": "Verify AI Design Quality Downloader",
        "description": "Verify download options for Low/High Resolution generated images.",
        "steps": "1. Click dropdown next to design download\n2. Select 'High Res (300dpi)'\n3. Verify file saved.",
        "expected": "File download begins, output is high resolution format."
    },
    {
        "id": "TC082",
        "tool": "Selenium",
        "category": "Results & AI Generation",
        "title": "Verify Vastu Re-analyze toggle inside result page",
        "description": "Verify user can change orientation quadrant directly in results page to re-score.",
        "steps": "1. Click 'Re-verify Vastu'\n2. Choose 'North-West' instead of 'South'\n3. Observe new Vastu score card update.",
        "expected": "Vastu score updates dynamically without full page refresh."
    },
    {
        "id": "TC083",
        "tool": "Selenium",
        "category": "Results & AI Generation",
        "title": "Verify Print Layout style rules",
        "description": "Ensure page prints cleanly without navigation sidebar components.",
        "steps": "1. Trigger print command (Ctrl+P / simulated print stylesheet)\n2. Inspect print preview media stylesheet rules.",
        "expected": "Navbars and settings are hidden from active print layout page."
    },
    {
        "id": "TC084",
        "tool": "Selenium",
        "category": "Results & AI Generation",
        "title": "Verify Detail expansion toggle on layout plans",
        "description": "Ensure clicking layout detail toggles visual outline schema.",
        "steps": "1. Click 'Layout Details'\n2. Verify display of furniture placements coordinates card.",
        "expected": "Layout scheme expansions animate smoothly."
    },
    {
        "id": "TC085",
        "tool": "Selenium",
        "category": "Results & AI Generation",
        "title": "Verify AI generation Timeout handler",
        "description": "Ensure client recovery UI displays if API doesn't return under 45 seconds.",
        "steps": "1. Mock backend slow response (>45s)\n2. Submit generation wizard\n3. Observe client UI warning.",
        "expected": "Displays 'Generation taking longer than expected. We will notify you once ready'."
    },
    {
        "id": "TC086",
        "tool": "Selenium",
        "category": "Project Management",
        "title": "Verify Projects Listing Grid",
        "description": "Ensure projects page displays all saved projects in a card layout.",
        "steps": "1. Go to `/projects`\n2. Verify project cards count\n3. Verify project name, date, and space type are shown.",
        "expected": "Saved designs populate the page layout properly."
    },
    {
        "id": "TC087",
        "tool": "Selenium",
        "category": "Project Management",
        "title": "Search and Filter Projects",
        "description": "Verify search bar dynamically filters matching project titles.",
        "steps": "1. Open `/projects`\n2. Type specific name in search bar\n3. Observe remaining project cards.",
        "expected": "Only cards with title containing search query remain visible."
    },
    {
        "id": "TC088",
        "tool": "Selenium",
        "category": "Project Management",
        "title": "Filter Projects by Room Type",
        "description": "Verify dropdown filter by category (e.g. Bedroom, Living Room).",
        "steps": "1. Open `/projects`\n2. Select 'Living Room' from Filter dropdown\n3. Verify card properties.",
        "expected": "Only Living Room projects are displayed in the dashboard grid."
    },
    {
        "id": "TC089",
        "tool": "Selenium",
        "category": "Project Management",
        "title": "Verify Project Detail Page Loading",
        "description": "Verify clicking a project card loads the specific detail view.",
        "steps": "1. Open `/projects`\n2. Click on card with id 'proj-123'\n3. Verify URL changes to `/project/proj-123`\n4. Inspect data.",
        "expected": "Loads design history, notes, and final generated images."
    },
    {
        "id": "TC090",
        "tool": "Selenium",
        "category": "Project Management",
        "title": "Add Notes to Project Detail",
        "description": "Verify user can append custom comments/notes to saved project.",
        "steps": "1. Open specific project detail page\n2. Write text in 'Notes' textarea\n3. Click 'Save Notes'\n4. Reload page and check if note persists.",
        "expected": "Notes are saved, page reloads with notes preserved."
    },
    {
        "id": "TC091",
        "tool": "Selenium",
        "category": "Project Management",
        "title": "Edit Project Title",
        "description": "Ensure user can rename their project.",
        "steps": "1. Open project detail page\n2. Click edit icon near title\n3. Rename to 'My Dream Living Room'\n4. Confirm edit.",
        "expected": "Title changes in UI and database."
    },
    {
        "id": "TC092",
        "tool": "Selenium",
        "category": "Project Management",
        "title": "Delete Project Confirmation",
        "description": "Ensure deletion request triggers a confirmation dialog box.",
        "steps": "1. Click Delete project button\n2. Verify dialog popup alert is shown.",
        "expected": "Dialog warns user of permanent loss with cancel/confirm options."
    },
    {
        "id": "TC093",
        "tool": "Selenium",
        "category": "Project Management",
        "title": "Complete Project Deletion",
        "description": "Verify confirming deletion removes item and redirects user.",
        "steps": "1. Click Delete\n2. Click Confirm on dialog\n3. Observe redirect.",
        "expected": "Redirected to dashboard; project no longer in grid."
    },
    {
        "id": "TC094",
        "tool": "Selenium",
        "category": "Project Management",
        "title": "Verify Batch Project Deletion option",
        "description": "Verify selecting multiple cards and deleting them works.",
        "steps": "1. Tick multiple check boxes on projects grid\n2. Click 'Delete Selected'\n3. Confirm dialog.",
        "expected": "All checked project cards disappear at once."
    },
    {
        "id": "TC095",
        "tool": "Selenium",
        "category": "Project Management",
        "title": "Verify Sorting Projects by Date and Title",
        "description": "Check if sorting options re-arrange cards correctly.",
        "steps": "1. Click sorting dropdown\n2. Select 'Oldest First'\n3. Verify card sequence.",
        "expected": "Cards sorted chronologically with oldest project first."
    },
    {
        "id": "TC096",
        "tool": "Selenium",
        "category": "Vastu Shastra Consultation",
        "title": "Verify Vastu page layout and form",
        "description": "Verify `/vastu` page renders Vastu-specific input questionnaire.",
        "steps": "1. Navigate to `/vastu`\n2. Verify checklist inputs: Main entrance, Bed placement, Mirror directions.",
        "expected": "Vastu entry form renders correctly with all compass direction buttons."
    },
    {
        "id": "TC097",
        "tool": "Selenium",
        "category": "Vastu Shastra Consultation",
        "title": "Verify Vastu recommendation generation",
        "description": "Submit vastu form and verify actionable tips display.",
        "steps": "1. Enter inputs on vastu page\n2. Click 'Analyze Room'\n3. Verify tips list display (e.g. 'Move mirror to North wall').",
        "expected": "Returns tailored Vastu tips based on input directions."
    },
    {
        "id": "TC098",
        "tool": "Selenium",
        "category": "Vastu Shastra Consultation",
        "title": "Interactive Compass Widget Verification",
        "description": "Verify compass graphic widget correctly maps orientations.",
        "steps": "1. Select compass directions\n2. Watch compass needle change angle dynamically.",
        "expected": "Interactive compass needle aligns with selected direction option."
    },
    {
        "id": "TC099",
        "tool": "Selenium",
        "category": "Vastu Shastra Consultation",
        "title": "Vastu Report Export option",
        "description": "Verify ability to copy Vastu text report or print page.",
        "steps": "1. Generate Vastu report\n2. Click 'Copy Report' or 'Print'\n3. Verify output.",
        "expected": "Text copied to clipboard or browser print dialog opens."
    },
    {
        "id": "TC100",
        "tool": "Selenium",
        "category": "Vastu Shastra Consultation",
        "title": "Verify Vastu checklist items save status",
        "description": "Ensure clicking check boxes keeps checked status on database profile save.",
        "steps": "1. Tick multiple checkboxes in vastu audit list\n2. Click 'Save Vastu Profile'\n3. Reload page.",
        "expected": "Checkboxes state persists on profile reload."
    },

    # ==========================================
    # APPIUM MOBILE TEST CASES (TC101 - TC200)
    # ==========================================
    {
        "id": "TC101",
        "tool": "Appium",
        "category": "Mobile Responsive Viewports",
        "title": "Verify Mobile Navigation Hamburger Icon Presence",
        "description": "Ensure mobile views hide navbar links behind a hamburger menu.",
        "steps": "1. Launch mobile driver\n2. Verify standard desktop navbar is hidden\n3. Verify hamburger menu button is present.",
        "expected": "Hamburger icon is present and header navigation is collapsed."
    },
    {
        "id": "TC102",
        "tool": "Appium",
        "category": "Mobile Responsive Viewports",
        "title": "Open Hamburger Menu Drawer Menu",
        "description": "Verify clicking hamburger expands the sidebar/drawer navigation.",
        "steps": "1. Click hamburger icon\n2. Verify drawer slides open\n3. Verify links visible in drawer.",
        "expected": "Drawer overlay slides in containing Dashboard, Projects, Vastu links."
    },
    {
        "id": "TC103",
        "tool": "Appium",
        "category": "Mobile Responsive Viewports",
        "title": "Close Hamburger Menu Drawer Widget",
        "description": "Verify closing drawer works by clicking close icon or clicking outside.",
        "steps": "1. Open drawer\n2. Tap outside the drawer area or click 'X'\n3. Verify drawer collapses.",
        "expected": "Drawer is hidden from screen layout."
    },
    {
        "id": "TC104",
        "tool": "Appium",
        "category": "Mobile Responsive Viewports",
        "title": "Verify Mobile Viewport scaling limits",
        "description": "Ensure viewport meta tag blocks initial user scale zoom issues on mobile.",
        "steps": "1. Load page on mobile device\n2. Verify content fits viewport width without horizontal scrollbars.",
        "expected": "No horizontal scrolling is required to read landing page content."
    },
    {
        "id": "TC105",
        "tool": "Appium",
        "category": "Mobile Responsive Viewports",
        "title": "Verify Card Layout column stacking on Mobile",
        "description": "Grid layouts must collapse to single column vertical stack on mobile width.",
        "steps": "1. Navigate to `/projects`\n2. Verify project cards display vertically stacked.",
        "expected": "Each project card occupies full width of the screen row."
    },
    {
        "id": "TC106",
        "tool": "Appium",
        "category": "Mobile Responsive Viewports",
        "title": "Verify Mobile Header Sticky positioning",
        "description": "Check if top nav stays fixed at the top of viewport during scroll down.",
        "steps": "1. Scroll down dashboard\n2. Verify top nav remains visible.",
        "expected": "Header menu bar is sticky at the top."
    },
    {
        "id": "TC107",
        "tool": "Appium",
        "category": "Mobile Responsive Viewports",
        "title": "Verify Font Scaling on small displays",
        "description": "Check that header texts do not wrap awkwardly or overlap on 360px displays.",
        "steps": "1. Configure screen viewport resolution to 360x640\n2. Inspect Hero title layouts.",
        "expected": "Fonts scale down properly; text remains clear."
    },
    {
        "id": "TC108",
        "tool": "Appium",
        "category": "Mobile Responsive Viewports",
        "title": "Verify Horizontal Scrollbars absence on Wizard page",
        "description": "Check that the multistep form doesn't cause overflow scrolling.",
        "steps": "1. Load wizard page\n2. Attempt horizontal scroll.",
        "expected": "Page content fits cleanly; no horizontal overflow detected."
    },
    {
        "id": "TC109",
        "tool": "Appium",
        "category": "Mobile Responsive Viewports",
        "title": "Verify Modal Popups Full Screen takeover on Mobile",
        "description": "Modals must take up full display width on mobile instead of fixed size.",
        "steps": "1. Trigger settings modal on mobile\n2. Inspect width settings.",
        "expected": "Modal takes 95% to 100% of horizontal viewport."
    },
    {
        "id": "TC110",
        "tool": "Appium",
        "category": "Mobile Responsive Viewports",
        "title": "Verify Footer Section stacking",
        "description": "Footer links should list vertically on mobile screen.",
        "steps": "1. Scroll to page bottom\n2. Inspect footer sections flex-direction.",
        "expected": "Footer sections are stacked vertically; alignment is centered."
    },
    {
        "id": "TC111",
        "tool": "Appium",
        "category": "Mobile Responsive Viewports",
        "title": "Verify Interactive icons size thresholds",
        "description": "Buttons must maintain 44px min touch space.",
        "steps": "1. Measure close icons and navigation triggers height/width.",
        "expected": "All elements meet mobile target boundaries."
    },
    {
        "id": "TC112",
        "tool": "Appium",
        "category": "Mobile Responsive Viewports",
        "title": "Verify Image grids stack layouts",
        "description": "Ensure design image gallery stacks cards.",
        "steps": "1. Go to gallery page\n2. Check column arrangement.",
        "expected": "Images stack vertically; page fits in viewport."
    },
    {
        "id": "TC113",
        "tool": "Appium",
        "category": "Mobile Responsive Viewports",
        "title": "Verify Back to Top button presence",
        "description": "Ensure scroll button displays after scrolling down two heights.",
        "steps": "1. Scroll down 1000px on landing page\n2. Verify floating arrow indicator shows up.",
        "expected": "Floating button appears in bottom corner."
    },
    {
        "id": "TC114",
        "tool": "Appium",
        "category": "Mobile Responsive Viewports",
        "title": "Verify Help floating bubble location",
        "description": "Ensure support bubble doesn't block important button layouts.",
        "steps": "1. Scroll through design wizard steps\n2. Verify support bubble positioning.",
        "expected": "Floating bubble stays in fixed corner and has high z-index."
    },
    {
        "id": "TC115",
        "tool": "Appium",
        "category": "Mobile Responsive Viewports",
        "title": "Verify Input fields default margins",
        "description": "Ensure text fields have enough spacing between them so they don't group together.",
        "steps": "1. Load form page\n2. Measure margin spacers.",
        "expected": "Form fields have consistent vertical separation margins."
    },
    {
        "id": "TC116",
        "tool": "Appium",
        "category": "Mobile User Authentication",
        "title": "Mobile Signup: Keyboard Input & Submit",
        "description": "Verify user can enter signup data on mobile and keyboard actions.",
        "steps": "1. Open `/signup` on mobile\n2. Tap email field (system keyboard displays)\n3. Enter credentials and click 'Done' on keyboard\n4. Submit.",
        "expected": "Mobile keyboard behaves correctly and user is signed up."
    },
    {
        "id": "TC117",
        "tool": "Appium",
        "category": "Mobile User Authentication",
        "title": "Mobile Login: Form Autofill Compatibility",
        "description": "Check that email and password fields support mobile keychain/autofill triggers.",
        "steps": "1. Tap email field on mobile login page\n2. Select keychain saved account\n3. Verify credentials fill.",
        "expected": "Form fields are successfully filled by mobile password manager."
    },
    {
        "id": "TC118",
        "tool": "Appium",
        "category": "Mobile User Authentication",
        "title": "Mobile Auth Route Protection check",
        "description": "Verify session loss redirects to login on mobile app launcher.",
        "steps": "1. Terminate app / clear localstorage\n2. Open app\n3. Verify `/login` is automatically shown.",
        "expected": "Redirected to login screen on launch."
    },
    {
        "id": "TC119",
        "tool": "Appium",
        "category": "Mobile User Authentication",
        "title": "Mobile Google Sign-In Integration",
        "description": "Verify Google authentication flow works inside mobile webview.",
        "steps": "1. Click Google Sign-in\n2. Handle Google account picker popup\n3. Verify back navigation and token exchange.",
        "expected": "User is authenticated and redirected back into webview container."
    },
    {
        "id": "TC120",
        "tool": "Appium",
        "category": "Mobile User Authentication",
        "title": "Mobile Logout and Cache Cleanup",
        "description": "Verify logout clears local storage and cookies on mobile.",
        "steps": "1. Tap settings -> Logout\n2. Verify localstorage session token is null.",
        "expected": "User session is completely removed from mobile localstorage."
    },
    {
        "id": "TC121",
        "tool": "Appium",
        "category": "Mobile User Authentication",
        "title": "Mobile password fields visual characters hide",
        "description": "Ensure password displays dots instead of plain characters on keyboard typing.",
        "steps": "1. Type character inside password box\n2. Check display value properties.",
        "expected": "Field obfuscates character immediately."
    },
    {
        "id": "TC122",
        "tool": "Appium",
        "category": "Mobile User Authentication",
        "title": "Mobile Forgot Password email trigger",
        "description": "Verify email recovery code works on mobile interface.",
        "steps": "1. Tap forgot password\n2. Submit email address\n3. Verify toast confirmation.",
        "expected": "Toast notification indicates code has been sent."
    },
    {
        "id": "TC123",
        "tool": "Appium",
        "category": "Mobile User Authentication",
        "title": "Mobile Resend Recovery Code countdown timer",
        "description": "Verify button resets after a cooldown timer.",
        "steps": "1. Submit recovery email\n2. Check 'Resend Code' status\n3. Wait 30 seconds.",
        "expected": "Resend code button displays a count down timer and changes state when ready."
    },
    {
        "id": "TC124",
        "tool": "Appium",
        "category": "Mobile User Authentication",
        "title": "Mobile Sign in validation focus shift",
        "description": "Ensure validation error focuses the first incorrect input block.",
        "steps": "1. Leave email empty and fill password\n2. Tap Login\n3. Check active cursor focus.",
        "expected": "Cursor focus shifts immediately to the empty email text input."
    },
    {
        "id": "TC125",
        "tool": "Appium",
        "category": "Mobile User Authentication",
        "title": "Mobile session persistence on app backgrounding",
        "description": "Ensure user remains logged in after sending app to background.",
        "steps": "1. Log in\n2. Send app to background for 10s\n3. Resume app foreground\n4. Verify current view.",
        "expected": "App loads on the dashboard; session is preserved."
    },
    {
        "id": "TC126",
        "tool": "Appium",
        "category": "Mobile User Authentication",
        "title": "Mobile Cookie policy consent dialog",
        "description": "Ensure cookies privacy modal accepts selections on mobile screens.",
        "steps": "1. Clear storage and reload app\n2. Click 'Accept Cookies' bottom sheet.",
        "expected": "Consent dialog sheet collapses smoothly."
    },
    {
        "id": "TC127",
        "tool": "Appium",
        "category": "Mobile User Authentication",
        "title": "Mobile Signup: Keyboard action key 'Next'",
        "description": "Ensure pressing 'Next' key on keyboard focuses password field.",
        "steps": "1. Fill email field\n2. Press 'Next' on soft keyboard\n3. Verify cursor focus location.",
        "expected": "Focus transitions immediately to Password field."
    },
    {
        "id": "TC128",
        "tool": "Appium",
        "category": "Mobile User Authentication",
        "title": "Mobile App version info display",
        "description": "Verify application version is visible in settings/about view.",
        "steps": "1. Go to settings\n2. Check footer text layout.",
        "expected": "Displays app version (e.g. v1.0.0)."
    },
    {
        "id": "TC129",
        "tool": "Appium",
        "category": "Mobile User Authentication",
        "title": "Mobile Secure token expiration callback",
        "description": "Verify application handles token expiration dynamically.",
        "steps": "1. Invalidate tokens\n2. Perform dashboard action\n3. Check redirection.",
        "expected": "Shows notification expired session and redirects to login."
    },
    {
        "id": "TC130",
        "tool": "Appium",
        "category": "Mobile User Authentication",
        "title": "Mobile Account Delete action safety",
        "description": "Verify deleting account prompts double password check.",
        "steps": "1. Tap Account Deletion button\n2. Verify text inputs require password validation.",
        "expected": "Deleter form requires confirmation steps."
    },
    {
        "id": "TC131",
        "tool": "Appium",
        "category": "Mobile Wizard Navigation",
        "title": "Mobile Wizard Step 1: Touch Target Size check",
        "description": "Verify room type select cards have a minimum touch target size of 48x48px.",
        "steps": "1. Open `/create`\n2. Inspect height and width of room selectors on mobile layout.",
        "expected": "Cards meet touch targets guidelines (min 48dp height/width)."
    },
    {
        "id": "TC132",
        "tool": "Appium",
        "category": "Mobile Wizard Navigation",
        "title": "Mobile Wizard Step 2: Theme Selection tap",
        "description": "Verify tapping theme card works cleanly on mobile screen.",
        "steps": "1. Proceed to style wizard step\n2. Tap 'Minimalist'\n3. Verify orange border highlight.",
        "expected": "Selection state updates instantly on tap."
    },
    {
        "id": "TC133",
        "tool": "Appium",
        "category": "Mobile Wizard Navigation",
        "title": "Mobile Wizard Step 3: Swipe Budget Selector bar",
        "description": "Verify budget range slider responds to drag and drop touch gestures.",
        "steps": "1. Press and hold slider thumb\n2. Drag thumb right on touch screen\n3. Verify budget value updates.",
        "expected": "Slider value increases as thumb is dragged."
    },
    {
        "id": "TC134",
        "tool": "Appium",
        "category": "Mobile Wizard Navigation",
        "title": "Mobile Wizard Step 4: Dimension numeric keypad check",
        "description": "Ensure dimension inputs launch numeric keypad, not standard qwerty.",
        "steps": "1. Tap length input box\n2. Verify mobile soft keyboard shows numbers-only template.",
        "expected": "Numeric keypad (`inputmode='numeric'`) is triggered on mobile."
    },
    {
        "id": "TC135",
        "tool": "Appium",
        "category": "Mobile Wizard Navigation",
        "title": "Mobile Wizard Step 5: Vastu direction selector grid",
        "description": "Verify direction buttons are large enough for thumb clicks.",
        "steps": "1. Go to Vastu page\n2. Tap directional quadrant button\n3. Verify selection.",
        "expected": "Selections occur without clicking adjacent direction buttons."
    },
    {
        "id": "TC136",
        "tool": "Appium",
        "category": "Mobile Wizard Navigation",
        "title": "Mobile Wizard Step 6: Native Camera Upload options",
        "description": "Verify clicking upload lets users choose between photo library or active camera.",
        "steps": "1. Tap upload button\n2. Verify system bottom sheet displays 'Take Photo' and 'Photo Library'.",
        "expected": "System image picker actions are available."
    },
    {
        "id": "TC137",
        "tool": "Appium",
        "category": "Mobile Wizard Navigation",
        "title": "Mobile Wizard: Cancel Wizard Flow modal",
        "description": "Ensure canceling wizard flow alerts users and goes back to dashboard.",
        "steps": "1. Tap 'Cancel' at top header\n2. Tap confirm on popup dialog\n3. Verify dashboard loads.",
        "expected": "Form is discarded, user returns to `/dashboard` safely."
    },
    {
        "id": "TC138",
        "tool": "Appium",
        "category": "Mobile Wizard Navigation",
        "title": "Mobile Wizard: Retain State on Screen Rotate option",
        "description": "Verify form selections do not reset on changing mobile orientation.",
        "steps": "1. Select 'Living Room' and 'Modern' style\n2. Rotate device to Landscape orientation\n3. Verify selections.",
        "expected": "UI updates layout dynamically; form data is intact."
    },
    {
        "id": "TC139",
        "tool": "Appium",
        "category": "Mobile Wizard Navigation",
        "title": "Mobile Wizard: Validation Alert Toasters style",
        "description": "Verify that input errors show up as easily readable toasts.",
        "steps": "1. Click next without filling current step\n2. Verify sonner/toast notification is visible at screen top.",
        "expected": "Toast notification alerts missing values."
    },
    {
        "id": "TC140",
        "tool": "Appium",
        "category": "Mobile Wizard Navigation",
        "title": "Mobile Wizard: Submit & Loading Indicator layout",
        "description": "Verify loading progress spinner stays centered on mobile view.",
        "steps": "1. Submit wizard details\n2. Observe spinner alignment on mobile screen.",
        "expected": "Spinner sits centered in the viewport."
    },
    {
        "id": "TC141",
        "tool": "Appium",
        "category": "Mobile Wizard Navigation",
        "title": "Mobile Wizard Room selection scroll selection",
        "description": "Ensure vertical swipe allows accessing bottom card categories.",
        "steps": "1. Swipe down on the room type lists\n2. Tap bottom item 'Study Room'.",
        "expected": "Study room card select highlights correctly."
    },
    {
        "id": "TC142",
        "tool": "Appium",
        "category": "Mobile Wizard Navigation",
        "title": "Mobile Wizard dimension numeric limit checks",
        "description": "Ensure dimensions above limit display standard inline mobile tooltip.",
        "steps": "1. Type '1000' in Length field\n2. Tap next\n3. Observe tooltip.",
        "expected": "Inline alert message 'Value exceeds maximum size' is shown."
    },
    {
        "id": "TC143",
        "tool": "Appium",
        "category": "Mobile Wizard Navigation",
        "title": "Mobile Wizard Step-indicator tapping shortcut",
        "description": "Tapping previous steps should navigate back if completed.",
        "steps": "1. Complete Step 1 and Step 2\n2. In Step 3, tap Step 1 circle indicator.",
        "expected": "Wizard slides back to Step 1 view."
    },
    {
        "id": "TC144",
        "tool": "Appium",
        "category": "Mobile Wizard Navigation",
        "title": "Mobile Wizard image deletion option",
        "description": "Ensure uploaded files can be removed via tap on close badge.",
        "steps": "1. Upload photo\n2. Click the small 'X' badge on preview item\n3. Observe list.",
        "expected": "File item disappears; upload button returns."
    },
    {
        "id": "TC145",
        "tool": "Appium",
        "category": "Mobile Wizard Navigation",
        "title": "Mobile Wizard custom budget text field sync",
        "description": "Typing budget triggers updates on slider positions.",
        "steps": "1. Tap budget input\n2. Type '12000'\n3. Check slider thumb location.",
        "expected": "Slider shifts automatically to match the typed value."
    },
    {
        "id": "TC146",
        "tool": "Appium",
        "category": "Mobile Wizard Navigation",
        "title": "Mobile Wizard Vastu compass coordinate touch selector",
        "description": "Ensure tapping exact angle values on Vastu ring rotates selector.",
        "steps": "1. Tap '270° West'\n2. Inspect highlighted label.",
        "expected": "Label West highlights; angle displays 270."
    },
    {
        "id": "TC147",
        "tool": "Appium",
        "category": "Mobile Wizard Navigation",
        "title": "Mobile Wizard blueprint check options",
        "description": "Tapping checklist item checks details.",
        "steps": "1. Go to blueprint step\n2. Tap checkbox 'Include electrical outlets'\n3. Verify toggle state.",
        "expected": "Checkbox selects correctly."
    },
    {
        "id": "TC148",
        "tool": "Appium",
        "category": "Mobile Wizard Navigation",
        "title": "Mobile Wizard Auto-save form draft",
        "description": "Ensure form progress is stored in local db if app closes.",
        "steps": "1. Fill Step 1 and 2\n2. Kill app process\n3. Launch app and navigate to `/create`.",
        "expected": "Form asks 'Restore draft progress?' option."
    },
    {
        "id": "TC149",
        "tool": "Appium",
        "category": "Mobile Wizard Navigation",
        "title": "Mobile Wizard draft restore flow",
        "description": "Ensure selecting restore draft populates previous inputs.",
        "steps": "1. Trigger draft options popup\n2. Click Restore\n3. Inspect selections.",
        "expected": "Form values restore to previous values."
    },
    {
        "id": "TC150",
        "tool": "Appium",
        "category": "Mobile Wizard Navigation",
        "title": "Mobile Wizard dismiss draft options",
        "description": "Ensure selecting discard draft clears details.",
        "steps": "1. Trigger draft options popup\n2. Click Discard\n3. Verify form fields.",
        "expected": "Form fields are clean and reset."
    },
    {
        "id": "TC151",
        "tool": "Appium",
        "category": "Mobile Wizard Navigation",
        "title": "Mobile Wizard theme categories segment filter",
        "description": "Ensure segment sliders toggle style presets.",
        "steps": "1. Go to Step 2\n2. Click 'Eastern Traditional' tab filter\n3. Verify visible theme cards.",
        "expected": "Theme list updates to show Vastu-focused options."
    },
    {
        "id": "TC152",
        "tool": "Appium",
        "category": "Mobile Wizard Navigation",
        "title": "Mobile Wizard file upload max limit indicator",
        "description": "Ensure file size warning appears if file is too large.",
        "steps": "1. Upload a 15MB design file\n2. Check validation toaster.",
        "expected": "Shows validation toast 'File exceeds maximum limit of 10MB'."
    },
    {
        "id": "TC153",
        "tool": "Appium",
        "category": "Mobile Wizard Navigation",
        "title": "Mobile Wizard help text tooltips",
        "description": "Ensure clicking help bubbles opens detail info popovers.",
        "steps": "1. Tap on info icon next to 'Vastu Directions'\n2. Inspect popover visibility.",
        "expected": "Info details popover expands smoothly."
    },
    {
        "id": "TC154",
        "tool": "Appium",
        "category": "Mobile Wizard Navigation",
        "title": "Mobile Wizard network connection drop dialog",
        "description": "Ensure submit is blocked if offline.",
        "steps": "1. Turn off mobile network\n2. Tap submit\n3. Verify feedback.",
        "expected": "Toast notification reads 'Network disconnected. Please check internet connection'."
    },
    {
        "id": "TC155",
        "tool": "Appium",
        "category": "Mobile Wizard Navigation",
        "title": "Mobile Wizard back header swipe nav",
        "description": "Ensure swiping right from screen edge navigates back in wizard.",
        "steps": "1. Perform swipe right gesture from left border edge\n2. Verify current step.",
        "expected": "Wizard returns to previous step."
    },
    {
        "id": "TC156",
        "tool": "Appium",
        "category": "Mobile Gesture Interactions",
        "title": "Swipe Landing Page testimonial Carousel",
        "description": "Verify swipe gestures navigate testimonial or image slider.",
        "steps": "1. Locate testimonials slider\n2. Execute swipe left gesture\n3. Verify next slide is active.",
        "expected": "Slider transitions to next image/review on left swipe gesture."
    },
    {
        "id": "TC157",
        "tool": "Appium",
        "category": "Mobile Gesture Interactions",
        "title": "Swipe down to refresh projects",
        "description": "Ensure pull down on projects lists triggers reload.",
        "steps": "1. Open `/projects`\n2. Drag list down from top border and release\n3. Verify loading overlay.",
        "expected": "List shows spinner and refreshes content from api."
    },
    {
        "id": "TC158",
        "tool": "Appium",
        "category": "Mobile Gesture Interactions",
        "title": "Swipe right to dismiss notification",
        "description": "Verify notification cards disappear on horizontal swiping.",
        "steps": "1. Open notifications card list\n2. Swipe right on top item\n3. Verify item presence.",
        "expected": "Card slides out of screen; toast confirms deletion."
    },
    {
        "id": "TC159",
        "tool": "Appium",
        "category": "Mobile Gesture Interactions",
        "title": "Pinch to zoom design preview image",
        "description": "Ensure users can pinch to zoom AI-generated interior images.",
        "steps": "1. Open generated design results page\n2. Do double-finger pinch gesture on image\n3. Verify image zooms in.",
        "expected": "AI image scales up according to gesture."
    },
    {
        "id": "TC160",
        "tool": "Appium",
        "category": "Mobile Gesture Interactions",
        "title": "Double tap photo to save",
        "description": "Verify double tap gesture saves image to device gallery.",
        "steps": "1. Open design image\n2. Perform double tap gesture\n3. Check photo permissions.",
        "expected": "Saves photo and displays 'Saved to Gallery' feedback."
    },
    {
        "id": "TC161",
        "tool": "Appium",
        "category": "Mobile Gesture Interactions",
        "title": "Swipe right slider tabs navigation",
        "description": "Verify swiping horizontally transitions tabs in dashboard.",
        "steps": "1. Load dashboard\n2. Swipe left on main panel content area\n3. Verify active tab shifts.",
        "expected": "Switches active tab from 'Projects' to 'Vastu Tools'."
    },
    {
        "id": "TC162",
        "tool": "Appium",
        "category": "Mobile Gesture Interactions",
        "title": "Long press project card to copy options",
        "description": "Ensure holding card opens quick options context list.",
        "steps": "1. Long press project card for 2 seconds\n2. Verify menu overlays.",
        "expected": "Quick actions modal displays options: rename, duplicate, delete."
    },
    {
        "id": "TC163",
        "tool": "Appium",
        "category": "Mobile Gesture Interactions",
        "title": "Drag and Drop list re-order",
        "description": "Verify holding drag icon on checklist items allows moving items vertically.",
        "steps": "1. Press and hold grabber icon next to checklist item 1\n2. Drag down below item 2\n3. Release.",
        "expected": "Order updates; item 1 displays below item 2."
    },
    {
        "id": "TC164",
        "tool": "Appium",
        "category": "Mobile Gesture Interactions",
        "title": "Swipe up to collapse dashboard stats summary",
        "description": "Scrolling lists down collapses stats to minimal layout.",
        "steps": "1. Scroll down project cards list\n2. Observe stats section size.",
        "expected": "Stats bar height decreases; project cards gain full viewport."
    },
    {
        "id": "TC165",
        "tool": "Appium",
        "category": "Mobile Gesture Interactions",
        "title": "Swipe left from sidebar edge to close drawer menu",
        "description": "Ensure sidebar can be closed with left swipe gesture.",
        "steps": "1. Open hamburger drawer\n2. Swipe left from inside menu drawer\n3. Verify drawer collapses.",
        "expected": "Drawer menu closes smoothly."
    },
    {
        "id": "TC166",
        "tool": "Appium",
        "category": "Mobile Integration",
        "title": "Deep Link navigation to specific Project page",
        "description": "Ensure opening 'krinterior://project/proj-123' launches app on target page.",
        "steps": "1. Trigger deep link scheme link\n2. Verify application launches\n3. Check if target project detail is displayed.",
        "expected": "App opens directly to the project detail view of 'proj-123'."
    },
    {
        "id": "TC167",
        "tool": "Appium",
        "category": "Mobile Integration",
        "title": "Deep Link navigation to Vastu screen",
        "description": "Verify deep link 'krinterior://vastu' opens Vastu section.",
        "steps": "1. Launch deep link for Vastu\n2. Verify current route is Vastu page.",
        "expected": "App displays Vastu Consultation view."
    },
    {
        "id": "TC168",
        "tool": "Appium",
        "category": "Mobile Integration",
        "title": "Invalid Deep Link handling redirections",
        "description": "Verify bad deep link falls back gracefully to dashboard.",
        "steps": "1. Trigger deep link 'krinterior://invalidpath'\n2. Verify application opens on dashboard.",
        "expected": "App opens dashboard and alerts user of invalid path request."
    },
    {
        "id": "TC169",
        "tool": "Appium",
        "category": "Mobile Integration",
        "title": "Mock push notification click redirect view",
        "description": "Verify clicking design ready push notification displays result screen.",
        "steps": "1. Simulate push notification 'Your AI Design is ready!'\n2. Click the notification\n3. Verify active screen.",
        "expected": "App launches and redirects user directly to the `/result` page."
    },
    {
        "id": "TC170",
        "tool": "Appium",
        "category": "Mobile Integration",
        "title": "OAuth Login Redirect back to App context",
        "description": "Verify Google auth browser page successfully returns user to native app shell.",
        "steps": "1. Click google login\n2. Browser completes OAuth and redirects to callback URL\n3. Verify app switches back to active foreground.",
        "expected": "App shell returns to foreground with logged-in user profile."
    },
    {
        "id": "TC171",
        "tool": "Appium",
        "category": "Mobile Integration",
        "title": "Verify deep link path parsing robustness",
        "description": "Check if extra slashes in custom scheme are parsed correctly.",
        "steps": "1. Launch link 'krinterior:///dashboard'\n2. Verify landing page redirect.",
        "expected": "App filters slashes and opens dashboard successfully."
    },
    {
        "id": "TC172",
        "tool": "Appium",
        "category": "Mobile Integration",
        "title": "Verify push notification payload structure",
        "description": "Ensure payload elements trigger deep links correctly.",
        "steps": "1. Trigger push with key/value 'route: vastu'\n2. Click alert.",
        "expected": "App redirects immediately to the `/vastu` path."
    },
    {
        "id": "TC173",
        "tool": "Appium",
        "category": "Mobile Integration",
        "title": "Verify offline token validation check",
        "description": "Ensure offline validation uses locally saved keystore tokens.",
        "steps": "1. Enable offline mode\n2. Launch application\n3. Check login status.",
        "expected": "User bypasses login; cached session holds."
    },
    {
        "id": "TC174",
        "tool": "Appium",
        "category": "Mobile Integration",
        "title": "Verify external store affiliate link handoff",
        "description": "Clicking store items must launch external browser, not in-app webview.",
        "steps": "1. Tap product link in budget sheet\n2. Verify system handler launches external browser app.",
        "expected": "Android OS opens Chrome/default browser outside app container."
    },
    {
        "id": "TC175",
        "tool": "Appium",
        "category": "Mobile Integration",
        "title": "Verify device share sheet menu options",
        "description": "Tapping share activates native social options list.",
        "steps": "1. Tap share icon\n2. Check if WhatsApp, Email, copy option populate layout.",
        "expected": "System share widgets list displays correctly."
    },
    {
        "id": "TC176",
        "tool": "Appium",
        "category": "Mobile Performance & UX",
        "title": "Verify Mobile Page Load Time (FCP) limits",
        "description": "Verify initial page load time on Simulated 3G/4G networks is fast.",
        "steps": "1. Configure Appium network speed to LTE\n2. Launch application\n3. Measure First Contentful Paint time.",
        "expected": "Page loads fully within 3 seconds on simulated LTE."
    },
    {
        "id": "TC177",
        "tool": "Appium",
        "category": "Mobile Performance & UX",
        "title": "Check App Offline mode banner alert",
        "description": "Ensure offline alert displays when mobile connection drops.",
        "steps": "1. Turn off device wifi/data in Appium emulator\n2. Verify top banner 'Offline Mode - using cached data' appears.",
        "expected": "Banner appears to keep user updated on connectivity status."
    },
    {
        "id": "TC178",
        "tool": "Appium",
        "category": "Mobile Performance & UX",
        "title": "Check App Online mode reconnect recovery layout",
        "description": "Verify recovery of app operations when network is restored.",
        "steps": "1. Restore wifi/data\n2. Observe banner disappearing\n3. Verify backend sync.",
        "expected": "Offline banner fades out, and pending local changes upload."
    },
    {
        "id": "TC179",
        "tool": "Appium",
        "category": "Mobile Performance & UX",
        "title": "Memory leak check on image canvas page detail",
        "description": "Verify image gallery pages do not crash after opening multiple designs.",
        "steps": "1. Navigate through 10 project details sequentially\n2. Observe memory consumption behavior in developer stats.",
        "expected": "Memory remains stable; no app crashes or freeze frames."
    },
    {
        "id": "TC180",
        "tool": "Appium",
        "category": "Mobile Performance & UX",
        "title": "Keyboard focus management on form transition elements",
        "description": "Verify focusing next input moves window viewport so keyboard doesn't block text.",
        "steps": "1. Tap First Input\n2. Tap Next field at bottom of form\n3. Verify field scrolls above screen keyboard area.",
        "expected": "Active text input is always visible above the virtual keyboard."
    },
    {
        "id": "TC181",
        "tool": "Appium",
        "category": "Mobile Performance & UX",
        "title": "Touch response latency check on buttons",
        "description": "Verify buttons have no 300ms click delay on modern mobile browser configurations.",
        "steps": "1. Tap Landing page CTA\n2. Measure time between click event and route change.",
        "expected": "Action initiates in less than 50ms."
    },
    {
        "id": "TC182",
        "tool": "Appium",
        "category": "Mobile Performance & UX",
        "title": "Verify image loading skeletons presence",
        "description": "Ensure design image cells render skeleton blocks during download.",
        "steps": "1. Force slow image api download\n2. Verify card elements placeholder.",
        "expected": "Gray skeleton panels pulse until images load."
    },
    {
        "id": "TC183",
        "tool": "Appium",
        "category": "Mobile Performance & UX",
        "title": "Verify low battery usage rendering guidelines",
        "description": "Ensure CSS animations pause when device goes into Low Power mode.",
        "steps": "1. Toggle device Low Power mode in emulator\n2. Inspect custom spin-slow animation states.",
        "expected": "High-intensity background frame layouts pause."
    },
    {
        "id": "TC184",
        "tool": "Appium",
        "category": "Mobile Performance & UX",
        "title": "Verify application crash logging integration",
        "description": "Ensure errors write logs in files.",
        "steps": "1. Force application runtime crash\n2. Check logs directory.",
        "expected": "Error log is recorded with device configuration."
    },
    {
        "id": "TC185",
        "tool": "Appium",
        "category": "Mobile Performance & UX",
        "title": "Verify clean app exit behavior",
        "description": "Verify clicking device back key twice at dashboard closes application.",
        "steps": "1. Go to dashboard\n2. Press back key twice rapidly\n3. Observe app state.",
        "expected": "Application closes; process goes to background."
    },
    {
        "id": "TC186",
        "tool": "Appium",
        "category": "Mobile Security",
        "title": "Token storage in Secure Storage keystores",
        "description": "Verify that authentication tokens are stored in Keychain / keystore rather than localstorage on native apps.",
        "steps": "1. Login inside app shell\n2. Inspect storage medium\n3. Verify token security.",
        "expected": "Tokens are securely isolated and not readable in plaintext web debuggers."
    },
    {
        "id": "TC187",
        "tool": "Appium",
        "category": "Mobile Security",
        "title": "Session Timeout auto logout trigger",
        "description": "Verify app logs out when session expires.",
        "steps": "1. Artificially expire the token in database\n2. Make request in app\n3. Verify user is returned to login screen.",
        "expected": "User is securely redirected to login screen with message."
    },
    {
        "id": "TC188",
        "tool": "Appium",
        "category": "Mobile Security",
        "title": "XSS script prevention in project title input box",
        "description": "Verify typing script tags in project title field does not trigger alert popup.",
        "steps": "1. Edit project title to `<script>alert('xss')</script>`\n2. Click Save\n3. Observe UI behavior.",
        "expected": "Title shows literal tags; no script execution occurs."
    },
    {
        "id": "TC189",
        "tool": "Appium",
        "category": "Mobile Security",
        "title": "Verify password obfuscation in screenshots",
        "description": "Ensure system screenshotting obscures login fields.",
        "steps": "1. Go to Login\n2. Take screen capture\n3. View saved capture.",
        "expected": "Password input area shows blacked out section."
    },
    {
        "id": "TC190",
        "tool": "Appium",
        "category": "Mobile Security",
        "title": "Verify SSL validation enforcement",
        "description": "Ensure application blocks connections if API endpoint lacks valid HTTPS cert.",
        "steps": "1. Redirect app to bad cert backend\n2. Check security warnings.",
        "expected": "App blocks connection and displays network error warning."
    },
    {
        "id": "TC191",
        "tool": "Appium",
        "category": "Mobile Security",
        "title": "Verify secure logout session deletion",
        "description": "Ensure back button after logout doesn't restore dashboard page.",
        "steps": "1. Click logout\n2. Click device hardware back button\n3. Verify view page.",
        "expected": "Main login page is shown; user is not logged back in."
    },
    {
        "id": "TC192",
        "tool": "Appium",
        "category": "Mobile Security",
        "title": "Verify API query param token injection block",
        "description": "Ensure authorization headers are used instead of query parameters.",
        "steps": "1. Request `/api/auth/me?token=xyz`\n2. Verify request rejects.",
        "expected": "Server returns 401 Unauthorized."
    },
    {
        "id": "TC193",
        "tool": "Appium",
        "category": "Mobile Accessibility",
        "title": "Screen Reader / TalkBack Labels compatibility check",
        "description": "Verify all interactive icons have valid accessibility content descriptions.",
        "steps": "1. Turn on TalkBack/VoiceOver\n2. Navigate through wizard\n3. Verify screen reader reads button descriptions.",
        "expected": "All buttons speak clear text labels (e.g. 'Back', 'Submit')."
    },
    {
        "id": "TC194",
        "tool": "Appium",
        "category": "Mobile Accessibility",
        "title": "Contrast Ratio compliance check on mobile design elements",
        "description": "Ensure text-to-background contrast ratio is at least 4.5:1 on smaller displays.",
        "steps": "1. Verify text colors on wizard page in mobile view against accessibility standards.",
        "expected": "Texts and buttons meet contrast safety guidelines."
    },
    {
        "id": "TC195",
        "tool": "Appium",
        "category": "Mobile Accessibility",
        "title": "Verify text size scaling alignment",
        "description": "Verify view layout doesn't break when user increases default OS text scale.",
        "steps": "1. Go to mobile settings, set font size to 'Extra Large'\n2. Open wizard step 1.",
        "expected": "Text stays within bounds; no component overlap occurs."
    },
    {
        "id": "TC196",
        "tool": "Appium",
        "category": "Mobile Accessibility",
        "title": "Verify Image alt attributes",
        "description": "Ensure all layout images possess alt attributes describing interior styles.",
        "steps": "1. Inspect DOM on results view\n2. Verify alt attributes presence.",
        "expected": "Alt tags contain text (e.g. 'Modern Living Room design')."
    },
    {
        "id": "TC197",
        "tool": "Appium",
        "category": "Mobile Accessibility",
        "title": "Verify keyboard focus tab order",
        "description": "Ensure tab navigation flows from top inputs to bottom buttons.",
        "steps": "1. Tab sequentially inside wizard form\n2. Verify element selection order.",
        "expected": "Tabbing proceeds left-to-right, top-to-bottom."
    },
    {
        "id": "TC198",
        "tool": "Appium",
        "category": "Mobile Accessibility",
        "title": "Verify tap sound feedback guidelines",
        "description": "Ensure tapping actions play standard click sound when device audios are on.",
        "steps": "1. Turn on device touch audios\n2. Click dashboard buttons.",
        "expected": "System plays standard click sound."
    },
    {
        "id": "TC199",
        "tool": "Appium",
        "category": "Mobile Accessibility",
        "title": "Verify Screen reader heading levels hierarchy",
        "description": "Verify headers are read sequentially (H1 -> H2 -> H3).",
        "steps": "1. Open Vastu screen\n2. Navigate headings using TalkBack.",
        "expected": "TalkBack reads structural headings correctly."
    },
    {
        "id": "TC200",
        "tool": "Appium",
        "category": "Mobile Accessibility",
        "title": "Verify touch targets minimal margins",
        "description": "Ensure buttons in headers have spacing to prevent accidental double clicks.",
        "steps": "1. Inspect margins between edit and delete options on project detail page.",
        "expected": "Margins are at least 8px."
    }
]


