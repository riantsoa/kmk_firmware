import digitalio
import microcontroller


def bootcfg(
    sense,
    source=None,
    no_cdc=True,
    no_hid=False,
    no_midi=True,
    no_storage=True,
    usb_id=None,
):

    if isinstance(sense, microcontroller.Pin):
        sense = digitalio.DigitalInOut(sense)
        sense.direction = digitalio.Direction.INPUT
        sense.pull = digitalio.Pull.UP

        if isinstance(source, microcontroller.Pin):
            source = digitalio.DigitalInOut(source)
            source.direction = digitalio.Direction.OUTPUT
            source.value = False
    else:
        return False

    # sense pulled low -> skip boot configuration
    if not sense.value:
        return False

    if no_cdc:
        import usb_cdc

        usb_cdc.disable()

    if no_hid:
        import usb_hid

        usb_hid.disable()

    if no_midi:
        import usb_midi

        usb_midi.disable()

    if isinstance(usb_id, tuple):
        import supervisor

        if hasattr(supervisor, 'set_usb_identification'):
            supervisor.set_usb_identification(*usb_id)

    # The no_storage entry is intentionally evaluated last to ensure the drive
    # is mountable and rescueable, in case any of the previous code throws an
    # exception.
    if no_storage:
        import storage

        storage.disable_usb_drive()

    return True
