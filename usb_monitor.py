import time
import usb.core
import usb.backend.libusb1
import libusb_package


def get_backend():
    return usb.backend.libusb1.get_backend(
        find_library=lambda x: libusb_package.find_library(x)
    )


def get_usb_devices():
    backend = get_backend()
    devices = usb.core.find(find_all=True, backend=backend)

    if devices is None:
        return set()

    return {
        (device.idVendor, device.idProduct)
        for device in devices
    }


previous_devices = get_usb_devices()

print("USB Device Monitor Started...")
print("Monitoring USB devices...")
print("Press Ctrl+C to stop.\n")


while True:
    current_devices = get_usb_devices()

    connected = current_devices - previous_devices
    disconnected = previous_devices - current_devices

    for vendor_id, product_id in connected:
        print(
            f"[CONNECTED] Vendor ID: {vendor_id:04x}, "
            f"Product ID: {product_id:04x}"
        )

    for vendor_id, product_id in disconnected:
        print(
            f"[DISCONNECTED] Vendor ID: {vendor_id:04x}, "
            f"Product ID: {product_id:04x}"
        )

    previous_devices = current_devices

    time.sleep(2)