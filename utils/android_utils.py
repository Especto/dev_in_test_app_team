import subprocess
import re

def android_get_desired_capabilities():
    return {
        'autoGrantPermissions': True,
        'automationName': 'uiautomator2',
        'newCommandTimeout': 500,
        'noSign': True,
        'platformName': 'Android',
        'platformVersion': '13',
        'resetKeyboard': True,
        'systemPort': 8301,
        'takesScreenshot': True,
        'udid': get_device_udid(),
        'connectTimeout': 30,
        'appPackage': 'com.ajaxsystems',
        'appActivity': 'com.ajaxsystems.ui.activity.LauncherActivity'
}


def get_device_udid():
    try:
        result = subprocess.run(["adb", "devices"], capture_output=True, text=True, check=True)

        udid_matches = re.findall(r'(\S+)\s+device\b', result.stdout, flags=re.MULTILINE)

        if udid_matches:
            return udid_matches[0]
        else:
            raise Exception("UDID not found.")

    except Exception as e:
        raise Exception(f"Error running 'adb devices': {e}")