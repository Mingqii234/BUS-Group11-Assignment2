from energy_alert import RoomStatus, EnergyAlertSystem
from main import scan_and_alert

def test_alert_triggered_for_empty_room_with_light(capsys):
    room = RoomStatus("TestRoom", is_occupied=False, light_on=True, ac_on=False)
    alerter = EnergyAlertSystem()
    alerter.update(room)
    captured = capsys.readouterr()
    assert "Alert: TestRoom is empty but light is ON!" in captured.out

def test_alert_triggered_for_empty_room_with_ac(capsys):
    room = RoomStatus("TestRoom", is_occupied=False, light_on=False, ac_on=True)
    alerter = EnergyAlertSystem()
    alerter.update(room)
    captured = capsys.readouterr()
    assert "Alert: TestRoom is empty but AC is ON!" in captured.out

def test_alert_triggered_for_both_devices(capsys):
    room = RoomStatus("TestRoom", is_occupied=False, light_on=True, ac_on=True)
    alerter = EnergyAlertSystem()
    alerter.update(room)
    captured = capsys.readouterr()
    assert "Alert: TestRoom is empty but light is ON and AC is ON!" in captured.out

def test_no_alert_if_room_occupied(capsys):
    room = RoomStatus("TestRoom", is_occupied=True, light_on=True, ac_on=True)
    alerter = EnergyAlertSystem()
    alerter.update(room)
    captured = capsys.readouterr()
    assert captured.out == ""

def test_no_alert_if_no_devices_on(capsys):
    room = RoomStatus("TestRoom", is_occupied=False, light_on=False, ac_on=False)
    alerter = EnergyAlertSystem()
    alerter.update(room)
    captured = capsys.readouterr()
    assert captured.out == ""

def test_scan_and_alert_mixed_rooms(capsys):
    alerter = EnergyAlertSystem()
    rooms = [
        RoomStatus("R1", False, True, False),
        RoomStatus("R2", True, True, False),
        RoomStatus("R3", False, False, True),
        RoomStatus("R4", False, True, True),
    ]
    scan_and_alert(rooms, alerter)
    captured = capsys.readouterr()
    out = [line.strip() for line in captured.out.strip().splitlines()]
    assert out == [
        "Alert: R1 is empty but light is ON!",
        "Alert: R3 is empty but AC is ON!",
        "Alert: R4 is empty but light is ON and AC is ON!"
    ]
