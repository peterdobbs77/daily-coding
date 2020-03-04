# consider a clock like the unit circle, with 12 as the zero position.


def calc_clock_angle(hours, minutes):
    h_deg = 30*(hours + (minutes/60)) % 360
    m_deg = 6*minutes  # convert minute hand to degrees around circle
    angle = abs(m_deg-h_deg)
    return angle


assert calc_clock_angle(12, 00) == 0
assert calc_clock_angle(6, 00) == 180
assert calc_clock_angle(1, 37) == abs(222 - 48.5)
