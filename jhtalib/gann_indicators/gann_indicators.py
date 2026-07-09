""""""
# Import Built-Ins:
import math

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


def GANN_SQUARE_OF_NINE(price, angle=45):
    """
    Gann Square of Nine - project a price by rotating it around the Square of Nine spiral.
    Theory: On Gann's Square of Nine, numbers spiral outward from 1 so that each
            complete 360-degree rotation advances the value by one full ring, i.e.
            the square root of the price increases by an additive, price-independent
            amount. Rotating clockwise from a value lands on the next square number
            after one revolution: 25 (=5^2) rotated 360 degrees becomes 49 (=7^2).
            The rotation is therefore additive on the square-root scale:
                target = (sqrt(price) + angle / 180.0) ** 2
            A full 360-degree turn adds 2.0 to the sqrt scale (moving n^2 -> (n+2)^2);
            180 degrees adds 1.0 (25 -> 36); 45 degrees adds 0.25 (100 -> 105.0625).
            Because the increment is additive it does not scale with price, and whole
            rotations are honored (360 degrees is never a no-op). Used to derive
            support/resistance and time-price targets.
    Returns: float (projected price at the given angle of rotation)
    Source: W.D. Gann - The Basis of My Forecasting Method; Square of Nine methodology
    """
    if price <= 0:
        return float('NaN')

    # Additive rotation on the square-root scale. Whole rotations are preserved
    # (no angle % 360), so each 360-degree turn advances one full ring.
    sqrt_price = math.sqrt(price)
    rotated_sqrt = sqrt_price + angle / 180.0
    result = rotated_sqrt ** 2

    return result
