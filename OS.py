def get_os():
    platformName = sys.platform

    if platformName == "win32":
        return "Windows"
    elif platformName == "darwin":
        return "Mac"
    elif platformName == "linux":
        return "Linux"
    else:
        return "Unknown"
