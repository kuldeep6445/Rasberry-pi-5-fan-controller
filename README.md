# Raspberry Pi 5 Fan Controller

This repository contains a Python script to control the fan speed of a Raspberry Pi 5 based on the CPU temperature. The script reads the current temperature and adjusts the fan speed accordingly to ensure efficient cooling.

## Files

- `fan_controller.py`: The main Python script that monitors the CPU temperature and adjusts the fan speed.

## Fan Speed Control

The fan speed is controlled based on the following temperature thresholds:

- Above 70°C: **Full Speed**
- 65°C to 70°C: **High Speed**
- 60°C to 65°C: **Medium Speed**
- 40°C to 60°C: **Low Speed**
- Below 40°C: **Off**

## Setup

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/rpi5-fan-controller.git
    cd rpi5-fan-controller
    ```

2. **Ensure the script is executable:**
    ```bash
    chmod +x fan_controller.py
    ```

3. **Set up the script to run on boot:**
    Add the following line to your crontab using `crontab -e`:
    ```bash
    @reboot python3 /root/fan_controller.py
    ```

4. **Reboot the Raspberry Pi to start the fan controller:**
    ```bash
    sudo reboot
    ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the Raspberry Pi community for the continuous support and resources.
