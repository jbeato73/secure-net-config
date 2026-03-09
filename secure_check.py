# =============================================================================
# secure_check.py
#
# Author  : Jose M. Beato
# Created : March 9, 2026
# Built with the assistance of Claude (Anthropic) — claude.ai
#
# Description:
#   Demonstrates secure credential management using environment variables
#   loaded from a .env file via python-decouple. Reads a controller URL
#   and API key, then performs an authenticated HTTP request to verify
#   the connection. Credentials are never hardcoded in source code.
#
# Dependencies:
#   pip install requests python-decouple
#
# Environment Variables (.env file required):
#   CONTROLLER_URL=https://your-controller-endpoint.com
#   API_KEY=your_api_key_here
#
# Project Setup (run in terminal before opening VS Code):
# ─────────────────────────────────────────────────────
#   1. cd /Users/jmb/PythonProjects
#   2. uv init secure-net-config
#   3. cd secure-net-config
#   4. code .
#   5. python3 -m venv .venv
#   6. source .venv/bin/activate
#   7. pip install requests python-decouple
#   # Create this file as: secure_check.py
#   # Create a .env file with CONTROLLER_URL and API_KEY before running.
#
# GitHub Commit (after completing):
# ──────────────────────────────────
#   git add secure_check.py
#   git commit -m "refactor: standardize secure_check.py header and structure"
#   git push origin main
# =============================================================================

from decouple import config, UndefinedValueError  # Third-party: .env loader
import requests                                    # Third-party: HTTP client


# =============================================================================
# SECTION 1 — CONFIGURATION
# Best Practice: Never hardcode credentials. config() reads from .env and
# raises UndefinedValueError if the variable is missing — which is safer
# than silently using an empty string.
# =============================================================================

# These are loaded at runtime from .env — never hardcoded in source code.
# Add a .env file to this directory with:
#   CONTROLLER_URL=https://your-endpoint.com
#   API_KEY=your-key-here


# =============================================================================
# SECTION 2 — CONNECTION LOGIC
# Best Practice: Wrap all external calls in try/except. Catch specific
# exceptions before the broad Exception fallback so each error type
# gets a meaningful message.
# =============================================================================


def connect_to_controller():
    """
    Loads credentials from environment variables and performs an
    authenticated HTTP GET request to the configured controller URL.

    Handles three error conditions:
      - Missing .env variables (UndefinedValueError)
      - Non-200 HTTP response (AUTH ERROR)
      - Any network or connection failure (RequestException)

    Returns:
        bool: True if connection succeeded, False otherwise.
    """
    print("[INFO] Initializing secure connection...")

    try:
        url     = config("CONTROLLER_URL")
        api_key = config("API_KEY")

        print(f"[INFO] Target: {url}")
        print("[INFO] Sending authenticated request...")

        headers  = {"Authorization": f"Bearer {api_key}"}
        response = requests.get(url, headers=headers, timeout=5)

        if response.status_code == 200:
            print("[INFO] CONNECTION SUCCESS — Controller is online and authenticated.")
            return True
        else:
            print(f"[WARN] AUTH ERROR — Received status {response.status_code}")
            return False

    except UndefinedValueError as e:
        print(f"[ERROR] Missing environment variable: {e}")
        print("        Check your .env file for CONTROLLER_URL and API_KEY.")
        return False
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Network error: {e}")
        return False
    except Exception as e:
        print(f"[ERROR] Unexpected error: {e}")
        return False


# =============================================================================
# SECTION 3 — SUMMARY PRINT
# Best Practice: Always print a human-readable summary to the console
# so you know what happened when you run the script.
# =============================================================================


def print_summary(success):
    """
    Prints a formatted connection summary to the console.

    Args:
        success (bool): Whether the connection attempt succeeded.
    """
    print()
    print("=" * 60)
    print("  SECURE NET CONFIG — SUMMARY REPORT")
    print("  Jose M. Beato | March 9, 2026")
    print("=" * 60)
    print(f"  Connection result : {'✅ SUCCESS' if success else '❌ FAILED'}")
    print(f"  Credentials from  : .env (not hardcoded)")
    print("=" * 60)
    print()


# =============================================================================
# SECTION 4 — MAIN ENTRY POINT
# Best Practice: Always use `if __name__ == "__main__"` to protect your
# main logic. This allows other scripts to import connect_to_controller()
# without automatically running the pipeline.
# =============================================================================


def main():
    """
    Orchestrates the full pipeline:
    Connect to Controller → Print Summary
    """
    print()
    print("=" * 60)
    print("  secure_check.py — Starting...")
    print("=" * 60)
    print()

    success = connect_to_controller()
    print_summary(success)


if __name__ == "__main__":
    main()

