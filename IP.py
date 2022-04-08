def validate_ip(ip_address: str):
    if len(ip_address) == 0:
        return False

    elements = ip_address.split(".")
    if len(elements) != 4 or not elements[0].isdigit() or int(elements[0]) > 253:
        return False

    for el in elements:
        if not el.isdigit() or (int(el) < 0 or int(el) > 255):
            return False

    return True
