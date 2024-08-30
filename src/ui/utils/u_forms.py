from PyQt5.QtWidgets import QLabel


def change_text_color(label: QLabel, color: str = "#ff13213b"):
    # change the color of the label
    label.setStyleSheet(f"color: {color}")


def check_form_inputs(obj, usr, pw, rpw):
    feedback = ""
    if not all([usr, pw, rpw]):
        feedback = "Alle Felder müssen ausgefüllt werden.\n"

    if len(pw) < 8:
        feedback = f"{feedback}Das Passwort muss mindestens 8 Zeichen lang sein.\n"

    if pw != rpw:
        feedback = f"{feedback}Das Wiederholungspasswort entspricht nicht dem Passwort"

    if feedback is not None:
        feedback = feedback.rstrip()
        obj.setText(feedback)
        change_text_color(label=obj, color="#ff0000")
        return False
    else:
        return True
