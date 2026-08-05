INVENTORY = {"gear": 12, "sprocket": 3}

def stock(name: str) -> int:
    return INVENTORY.get(name, 0)


def page(names, size: int = 10):
    return names[:size]
