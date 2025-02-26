from unittest.mock import Mock, patch

import pytest

from pitop.pma.common.servo_motor_registers import (
    ServoMotorS0,
    ServoMotorSetup,
    ServoRegisterTypes,
)


@pytest.fixture
def servo_controller():
    plate_interface_patch = patch("pitop.pma.servo_controller.PlateInterface")
    plate_interface_patch.start()

    from pitop.pma.servo_controller import ServoController

    yield ServoController

    plate_interface_patch.stop()


def test_constructor_success(servo_controller):
    controller = servo_controller(port="S0")
    assert controller.registers == ServoMotorS0


def test_constructor_fails_on_incorrect_port(servo_controller):
    """Constructor fails if providing an invalid port."""
    with pytest.raises(Exception):
        servo_controller(port="invalid_port")


def test_set_min_pulse_width_write(servo_controller):
    """Registers written when setting the minimum pulse width to MCU."""
    # create instance
    controller = servo_controller(port="S1")
    # setup mock
    with patch.object(controller._mcu_device, "write_word") as write_word_mock:
        min_pulse_width = 500
        # test
        controller.set_min_pulse_width(min_pulse_width)
        write_word_mock.assert_called_with(
            ServoMotorSetup.REGISTER_MIN_PULSE_WIDTH,
            min_pulse_width,
            signed=False,
            little_endian=True,
        )


def test_set_max_pulse_width_write(servo_controller):
    """Registers written when setting the maximum pulse width to MCU."""
    # create instance
    controller = servo_controller(port="S1")
    # setup mock
    with patch.object(controller._mcu_device, "write_word") as write_word_mock:
        max_pulse_width = 500
        # test
        controller.set_max_pulse_width(max_pulse_width)
        write_word_mock.assert_called_with(
            ServoMotorSetup.REGISTER_MAX_PULSE_WIDTH,
            max_pulse_width,
            signed=False,
            little_endian=True,
        )


def test_set_pwm_frequency_read_write(servo_controller):
    """Registers read/written when setting/reading PWM frequency to/from
    MCU."""
    # create instance
    controller = servo_controller(port="S0")

    pwm_frequency_value = 200
    with patch.object(controller, "_mcu_device") as mcu_device_mock:
        # setup r/w mocks
        write_byte_mock = mcu_device_mock.write_byte = Mock()
        read_unsigned_byte_mock = mcu_device_mock.read_unsigned_byte = Mock(
            return_value=pwm_frequency_value
        )

        # test
        controller.set_pwm_frequency(pwm_frequency_value)
        write_byte_mock.assert_called_with(
            ServoMotorSetup.REGISTER_PWM_FREQUENCY, pwm_frequency_value
        )

        assert controller.pwm_frequency() == pwm_frequency_value
        read_unsigned_byte_mock.assert_called_with(
            ServoMotorSetup.REGISTER_PWM_FREQUENCY
        )


def test_acceleration_mode_read_write(servo_controller):
    """Registers read/written when setting/reading acceleration mode to/from
    MCU."""
    # create instance
    controller = servo_controller(port="S0")

    with patch.object(controller, "_mcu_device") as mcu_device_mock:
        for acceleration_mode in (0, 1):
            # setup r/w mocks
            write_byte_mock = mcu_device_mock.write_byte = Mock()
            read_unsigned_byte_mock = mcu_device_mock.read_unsigned_byte = Mock(
                return_value=acceleration_mode
            )

            # test
            controller.set_acceleration_mode(acceleration_mode)
            write_byte_mock.assert_called_with(
                ServoMotorS0.get(ServoRegisterTypes.ACC_MODE), acceleration_mode
            )

            assert controller.get_acceleration_mode() == acceleration_mode
            read_unsigned_byte_mock.assert_called_with(
                ServoMotorS0.get(ServoRegisterTypes.ACC_MODE)
            )


def test_acceleration_mode_fails_on_invalid_type(servo_controller):
    """Can't set acceleration mode if provided mode has invalid type."""
    controller = servo_controller(port="S0")

    for acceleration_mode in ("a", 0.1):
        with pytest.raises(TypeError):
            controller.set_acceleration_mode(acceleration_mode)
