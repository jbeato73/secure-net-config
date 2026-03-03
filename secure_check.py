from decouple import config, UndefinedValueError
import requests


def connect_to_controller():
    print("🔐 Initializing Secure Connection...")

    try:
        # Fetching secrets from .env (NOT hardcoded)
        url = config("CONTROLLER_URL")
        api_key = config("API_KEY")

        print(f"📡 Target acquired: {url}")

        # Simulating a secure API call
        headers = {"Authorization": f"Bearer {api_key}"}

        # For this practice, we'll hit a public test API but use our 'secrets'
        print("🚀 Sending authenticated request...")
        response = requests.get("https://httpbin.org/get", headers=headers, timeout=5)

        if response.status_code == 200:
            print("✅ CONNECTION SUCCESS: Controller is online and authenticated.")
        else:
            print(f"❌ AUTH ERROR: Received status {response.status_code}")

    except UndefinedValueError:
        print("🚨 CRITICAL ERROR: Environment variables missing! Check your .env file.")
    except Exception as e:
        print(f"🚨 UNEXPECTED ERROR: {e}")


if __name__ == "__main__":
    connect_to_controller()
