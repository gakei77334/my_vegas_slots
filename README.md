# MyVegas App Automation Script

This Python script automates the MyVegas Slots game using ADB (Android Debug Bridge) and PIL (Python Imaging Library). It performs various tasks to manage in-game activities to continuously collect reward points, watch ads for more points and shuts down when all available points have been collected.

**Key Features:**
* Device Interaction: Wakes the device, unlocks it, and navigates to the MyVegas app.
* Automated Workflow: Manages gameplay by collecting rewards, handling ads, and resolving in-game issues.
* Pixel Color Analysis: Uses screenshots and pixel color analysis to make decisions based on visual cues within the app.
* Scheduled Operations: Executes tasks periodically, including putting the device to sleep and resuming activities.

**Technologies Used:**
* Python
* ADB (Android Debug Bridge)
* PIL (Python Imaging Library)
* NumPy

**Automated Actions:**
The script performs the following actions in a continuous loop:
* Wakes the device and unlocks it using swipe gestures.
* Opens the MyVegas app and navigates to specific sections.
* Checks for and dismisses ads to optimize gameplay.
* Collects daily bonuses and other in-game rewards automatically.
* Handles connection timeouts and other system errors.
* Monitors and interacts with in-game elements using pixel color analysis.

**Pixel Color Analysis:**
* Captures screenshots at predefined coordinates.
* Analyzes specific pixel values to detect UI elements such as green ticks and ad indicators.
* Triggers corresponding actions based on the analyzed pixel colors to progress through gameplay effectively.
