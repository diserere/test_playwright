pytest-playwright Tests
---

This repository contains automated tests written using [pytest](https://docs.pytest.org/) and [Playwright](https://playwright.dev/python/), which I'm developing while learning how to use Playwright in combination with pytest for end-to-end browser testing.

This project is designed to serve as a practical learning resource and a foundation for writing reliable, maintainable web automation tests.


## Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8+** (3.12 tested on my environment)
- **pip** (Python package installer)
- **git** (optional, for cloning the repository)


## Installation

Follow these steps to set up the project in a virtual environment:

1. Clone the repository (optional)

   ```bash
   git clone https://github.com/diserere/test_playwright.git
   cd test_playwright
   ```

2. Create a virtual environment

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

   - On Windows:

     ```cmd
     venv\Scripts\activate
     ```

   > [!WARNING]
   > All the following steps should be performed into virtual environment!


4. Upgrade pip (recommended)

   ```bash
   pip install --upgrade pip
   ```


5. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```

6. Install Playwright browser binaries

   ```bash
   playwright install
   ```

   This command installs the required browsers (Chromium, Firefox, WebKit) used by Playwright.


## Running Tests

Once everything is set up, you can run the tests using:

```bash
pytest
```

Optional: Run with verbose output:
```bash
pytest -v
```

Run a specific test file:
```bash
pytest tests/test_example.py
```

Run tests in headed mode (visible browser):
```bash
pytest --headed
```

Run tests on a specific browser:
```bash
pytest --browser chromium
pytest --browser firefox
pytest --browser webkit
```


## Project Structure
```
test_playwright/  
├── allure_regenerate_w_hist.sh
├── config/
│   └── setup_logging/
│       └── __init__.py
├── conftest.py
├── logs/
├── pytest.ini
├── README.md
├── requirements.txt
├── sample_page.html
└── tests/
    └── test_sample.py
```

- tests/ - contains test scripts.
- logs/ - directory for pytest `pytest_session.log` file (configured to DEBUG log level, added to .gitignore).
- conftest.py -  configuration and fixtures for pytest.
- pytest.ini - configuration file with pytest settings.
- sample_page.html - some simple html page with samples of some elements, e.g. selects.
- allure_regenerate_w_hist.sh - script to generate allure report (requires allure binary to be installed for your OS).


## Learning Resources
[Playwright Python Documentation](https://playwright.dev/python/)


## Contributing
As this is a personal learning project, contributions are not currently accepted. However, feel free to fork the repo and use it for your own learning!


## License
This project is open-source and available for personal and educational use.

---

Happy testing! 

## Test Markdown

> [!NOTE]
> Highlights information that users should take into account, even when skimming.

> [!TIP]
> Optional information to help a user be more successful.

> [!IMPORTANT]
> Crucial information necessary for users to succeed.

> [!WARNING]
> Critical content demanding immediate user attention due to potential risks.

> [!CAUTION]
> Negative potential consequences of an action.
