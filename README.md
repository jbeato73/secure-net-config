# Secure Network Configurator

A Python-based utility demonstrating enterprise-standard **Secret Management**. This project separates sensitive infrastructure credentials (API Keys, Controller URLs) from the application logic using environment variables.

## Security Features
* **Zero-Exposure Policy:** Uses `.gitignore` to ensure private credentials in `.env` are never committed to version control.
* **Environment Decoupling:** Leverages `python-decouple` to manage configurations across different environments (Dev, Test, Prod).
* **Fail-Safe Validation:** Implements `UndefinedValueError` handling to prevent the script from executing if mandatory security tokens are missing.

## Architecture
Instead of hardcoding sensitive data, the script pulls configuration from a hidden local file. This follows the **12-Factor App** methodology for modern software development.

## Installation & Setup

1. **Clone the repository and sync dependencies:**
   ```bash
   uv sync

2. **Initialize your environment variables:**

The repository includes a template file. Copy it to create your private .env file:

Bash
cp .env.example .env

3. **Configure your secrets:**

Open the new .env file and replace the placeholder values with your actual controller credentials:

Plaintext
CONTROLLER_URL=[https://your-sdwan-api.com](https://your-sdwan-api.com)
API_KEY=your_actual_secret_token

4. **Run the Secure Check:**

Bash
uv run python secure_check.py


# Dependency Stack
. python-decouple: For robust environment variable management.

. requests: For authenticated API communication.
