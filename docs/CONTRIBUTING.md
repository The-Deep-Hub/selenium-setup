# Contributing to Selenium WebDriver Setup Library

We welcome contributions to the Selenium WebDriver Setup Library, whether it's bug reports, feature requests, or pull requests. Follow the guidelines below to contribute to the project.

## Table of Contents

- [Reporting Issues](#reporting-issues)
- [Feature Requests](#feature-requests)
- [Code Contributions](#code-contributions)
  - [Fork the Repository](#fork-the-repository)
  - [Clone Your Fork](#clone-your-fork)
  - [Set Up Your Environment](#set-up-your-environment)
  - [Create a Branch](#create-a-branch)
  - [Make Your Changes](#make-your-changes)
  - [Run Tests](#run-tests)
  - [Submit Your Changes](#submit-your-changes)
- [Areas for Contribution](#areas-for-contribution)
- [Coding Guidelines](#coding-guidelines)

## Reporting Issues

If you encounter any bugs, crashes, or unexpected behavior, feel free to open an issue on the repository. Please include:

1. A detailed description of the issue.
2. Steps to reproduce the issue.
3. The expected outcome and what actually happens.
4. Any relevant log output or error messages.

We appreciate bug reports with as much detail as possible.

## Feature Requests

If you have an idea for an enhancement or a new feature, open an issue with the label `enhancement`. Please include a clear description of the feature, how it improves the project, and any relevant examples or use cases.

## Code Contributions

We love seeing contributions from the community. Follow these steps to submit code changes:

### Fork the Repository

1. Go to the project’s [GitHub repository](https://github.com/The-Deep-Hub/selenium-setup.git) and click the "Fork" button to create your own copy of the repository.

### Clone Your Fork

2. Clone your fork locally using the following command:

   ```bash
   git clone https://github.com/The-Deep-Hub/selenium-setup.git
   ```

3. Change into the project directory

    ```bash
    cd yourproject
    ```

### Set up your enviroment 

4. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5. Set up any other environment settings if necessary (e.g., database configuration, environment variables).

### Create a branch

6. Always create a new branch for your work. Never work directly on the main or master branch. You can create a branch with the following command:

    ```bash
    git checkout -b feature-branch-name
    ```

    Use a meaningful name for your branch that reflects the work you are doing (e.g., ```fix-logging-issue``` or ```add-firefox-support```).    

### Make Your Changes

7. Make your changes in the branch you just created.

8. Follow the Coding Guidelines to ensure your code is clean and maintainable.

### Run tests

9. Ensure that all tests pass before submitting your changes. If you’ve added new features or fixed bugs, make sure to include test coverage.

    ```bash
    pytest
    ```

    If you haven't already, write tests for any new functionality or changes you've made.

### Submit Your Changes

10. Once your changes are complete and tested, commit them with a descriptive message:

    ```bash
    git commit -m "Description of the change made"
    ```

11. Push your branch to your forked repository:

    ```bash
    git push origin feature-branch-name
    ```

12. Go to the original repository on GitHub and open a pull request from your fork. Provide a detailed description of what you've changed and any related issues.

## Areas for Contribution

We encourage contributions in the following areas:

1. **Adding New Browser Support:** If there is a browser that isn't currently supported (e.g., Opera, Safari, or other custom browsers), feel free to contribute by adding support for it. This would typically involve implementing a new setup class that extends BaseDriverSetup.

2. **Adding New WebDriver Options:** If there are WebDriver options that are not currently implemented in WebDriverSetup, feel free to add them. Examples include custom preferences, debugging flags, or more advanced network configurations.

3. **Improving Error Handling:** Enhancing the error-handling mechanisms in the library to provide better recovery options, retries, and error reporting.

**4.Documentation Improvements:** If you find areas where documentation could be improved or expanded, feel free to contribute. This includes better descriptions, usage examples, or even tutorials.

5. **Refactoring:** If you find areas of the codebase that could be optimized or simplified, we appreciate contributions that maintain or improve performance and readability.

6. **Writing More Unit Tests:** Help expand the test coverage by writing additional unit tests, especially for edge cases or newly added features.

7. **Bug Fixes:** If you encounter any bugs, feel free to submit a pull request with a fix, along with a description of the issue.

## Coding Guidelines

To maintain consistency across the codebase, please follow these coding guidelines:

Use meaningful variable and function names.
- Maintain consistency in code formatting (e.g., indentation, line breaks).
- Follow PEP 8 for Python code style.
- Ensure your code is well-documented, with comments and docstrings where applicable.
- Keep functions and methods small and focused on a single task.
- Write unit tests for new code and ensure existing tests pass.

Thank you for your interest in contributing to the Selenium WebDriver Setup Library! We look forward to your contributions.