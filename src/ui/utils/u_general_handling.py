from typing import Any


def create_and_set_obj_property(
    obj: Any, property_type: str = None, property_value: Any = None
) -> Any:
    if property_type is not None:
        setattr(obj, property_type, property_value)
        obj.setProperty(property_type, property_value)
    return obj
