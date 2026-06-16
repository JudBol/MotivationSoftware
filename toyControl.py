"""Device Control - Vibrate, rotate, and position commands.

This example shows how to control different types of devices:
- Vibrators: Set vibration intensity
- Rotators: Set rotation speed
- Strokers: Move to position over time

The example checks what each device supports before sending commands,
so it will work with any device type.

Prerequisites:
1. Install Intiface Central: https://intiface.com/central/
2. Start Intiface Central and click "Start Server"
3. Have a supported device connected
4. Run this script: python device_control.py
"""

import asyncio

from buttplug import ButtplugClient, DeviceOutputCommand, OutputType


async def main() -> None:   #reference code i will draw form
    client = ButtplugClient("Device Control Example")

    # Set up event handlers to see devices as they connect
    client.on_device_added = lambda d: print(f"Device connected: {d.name}")
    client.on_device_removed = lambda d: print(f"Device disconnected: {d.name}")

    print("Connecting to server...")
    await client.connect("ws://127.0.0.1:12345")

    print("Scanning for devices (5 seconds)...")
    await client.start_scanning()
    await asyncio.sleep(5)
    await client.stop_scanning()

    if not client.devices:
        print("No devices found!")
        await client.disconnect()
        return

    # Control each device based on its capabilities
    for device in client.devices.values():
        print(f"\nControlling: {device.name}")

        # Vibration
        if device.has_output(OutputType.VIBRATE):
            print("  Starting vibration at 25%...")
            await device.run_output(DeviceOutputCommand(OutputType.VIBRATE, 0.25))
            await asyncio.sleep(1)

            print("  Increasing to 50%...")
            await device.run_output(DeviceOutputCommand(OutputType.VIBRATE, 0.5))
            await asyncio.sleep(1)

            print("  Full power (100%)...")
            await device.run_output(DeviceOutputCommand(OutputType.VIBRATE, 1.0))
            await asyncio.sleep(1)

        # Rotation
        if device.has_output(OutputType.ROTATE):
            print("  Rotating at 50%...")
            await device.run_output(DeviceOutputCommand(OutputType.ROTATE, 0.5))
            await asyncio.sleep(2)

        # Position (strokers/linear devices)
        if device.has_output(OutputType.POSITION_WITH_DURATION):
            print("  Moving to top position...")
            await device.run_output(
                DeviceOutputCommand(OutputType.POSITION_WITH_DURATION, 1.0, duration=500)
            )
            await asyncio.sleep(1)

            print("  Moving to bottom position...")
            await device.run_output(
                DeviceOutputCommand(OutputType.POSITION_WITH_DURATION, 0.0, duration=500)
            )
            await asyncio.sleep(1)

            print("  Moving to middle...")
            await device.run_output(
                DeviceOutputCommand(OutputType.POSITION_WITH_DURATION, 0.5, duration=250)
            )
            await asyncio.sleep(1)

        # Stop the device
        print("  Stopping device...")
        await device.stop()

    print("\nAll done!")
    await client.disconnect()

"""
from here on is my own code

the idea of this is to make a simple set of functions to control the vibe
yes it will be rough lmao

imma add it so that it's continuous in terms of vibes, ie the vibe doesnt disconnect until later
"""
def testVibrate() -> None:
    asyncio.run(main())

async def limitVibe(invibe): #limits inputs to between 0 and 1 #check me for when things break/get slow
    return min(max(invibe, 0), 1)


async def vibeAtPower( vibe_power : float ) -> None: #doing the whole connection/disconnect thing

    client = ButtplugClient("Device Control Example")

    # Set up event handlers to see devices as they connect
    client.on_device_added = lambda d: print(f"Device connected: {d.name}")
    client.on_device_removed = lambda d: print(f"Device disconnected: {d.name}")

    print("Connecting to server...")
    await client.connect("ws://127.0.0.1:12345")

    print("Scanning for devices (5 seconds)...")
    await client.start_scanning()
    await asyncio.sleep(5)
    await client.stop_scanning()

    if not client.devices:
        print("No devices found!")
        await client.disconnect()
        return

    # Control each device based on its capabilities
    for device in client.devices.values():
        print(f"\nControlling: {device.name}")

        # Vibration
        if device.has_output(OutputType.VIBRATE):
            vibe_power = await limitVibe(vibe_power)
            print(f"  Starting vibration at {vibe_power*100}%...")

            await device.run_output(DeviceOutputCommand(OutputType.VIBRATE, vibe_power))

            battery = await device.battery()
            print(f"  Battery: {battery*100}%")

            await asyncio.sleep(1)

        # Stop the device
        print("  Stopping device...")
        await device.stop()

    print("\nAll done!")
    await client.disconnect()

async def vibeAtPowerExperiment(vibe_power: float) -> None:  # doing the whole connection/disconnect thing

    client = ButtplugClient("Device Control Example")

    # Set up event handlers to see devices as they connect
    client.on_device_added = lambda d: print(f"Device connected: {d.name}")
    client.on_device_removed = lambda d: print(f"Device disconnected: {d.name}")

    print("Connecting to server...")
    await client.connect("ws://127.0.0.1:12345")

    print("Scanning for devices (5 seconds)...")
    await client.start_scanning()
    await asyncio.sleep(5)
    await client.stop_scanning()

    if not client.devices:
        print("No devices found!")
        await client.disconnect()
        return

    # Control each device based on its capabilities
    for device in client.devices.values():
        print(f"\nControlling: {device.name}")

        # Vibration
        if device.has_output(OutputType.VIBRATE):
            vibe_power = await limitVibe(vibe_power)
            print(f"  Starting vibration at {vibe_power * 100}%...")

            await device.run_output(DeviceOutputCommand(OutputType.VIBRATE, vibe_power))

            battery = await device.battery()
            print(f"  Battery: {battery * 100}%")

            await asyncio.sleep(1)

        # Stop the device
        print("  Stopping device...")
        await device.stop()

    print("\nAll done!")
    await client.disconnect()



def vibrateAtPower(vibePower : float ) -> None:
    asyncio.run(vibeAtPower(vibePower))

def vibrateAtPowerExperimental(vibePower: float) -> None:
    asyncio.run(vibeAtPowerExperiment(vibePower))


if __name__ == "__main__":
    vibrateAtPower(0.5)