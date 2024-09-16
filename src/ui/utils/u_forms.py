from PyQt5.QtWidgets import QLabel, QWidget


def change_text_color(label: QLabel, color: str = "#ff13213b"):
    # change the color of the label
    label.setStyleSheet(f"color: {color}")


def check_form_inputs(obj, usr, pw, rpw):
    feedback: str = ""
    if not all([usr, pw, rpw]):
        feedback = "Alle Felder müssen ausgefüllt werden.\n"

    if len(pw) < 8:
        feedback = f"{feedback}Das Passwort muss mindestens 8 Zeichen lang sein.\n"

    if pw != rpw:
        feedback = f"{feedback}Das Wiederholungspasswort entspricht nicht dem Passwort"

    if feedback != "":
        feedback = feedback.rstrip()
        obj.setText(feedback)
        change_text_color(label=obj, color="#ff0000")
        return False
    else:
        return True


def get_widget_index(stacked_widget: QWidget, widget_name: str = None) -> int:
    """
    Returns the index of the given widget in the stacked widget.
    If no widget name is provided, the function returns the index of the current active widget.

    :param stacked_widget: The stacked widget containing the widgets.
    :type stacked_widget: QWidget
    :param widget_name: The name of the widget to find. (optional)
    :type widget_name: str
    :return: The index of the widget in the stacked widget.
    :rtype: int
    """

    try:
        widget: QWidget = stacked_widget.findChild(QWidget, widget_name)
        return stacked_widget.indexOf(widget)
    except Exception as e:
        raise RuntimeError(f"Failed to find widget: {str(e)}")
