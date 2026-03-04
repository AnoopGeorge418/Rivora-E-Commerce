import bcrypt, string, random

class AppUtilities:
    """Generates utilities required for Phone Auth"""
    
    @staticmethod
    def generate_hashed_password(max_length: int = 12) -> str:
        """
            Generates a strong hashed password.
            Args: 
                max_lenght (int) -> Length of the password to generate
                    A larger value increases password strength.
            Returns:
                str: hahed password
        """
        chars = (
            string.ascii_lowercase +
            string.ascii_uppercase +
            string.digits +
            string.punctuation
        )
        raw_password = "".join(random.choice(chars)for _ in range(max_length))
        hashed_password = bcrypt.hashpw( raw_password.encode(), bcrypt.gensalt(max_length) )

        return hashed_password.decode()

    @staticmethod
    def generate_hashed_otp(max_lenght: int = 6) -> tuple[int, str]:
        """Generates a hashed otp.

        Args:
            max_lenght (int): Length of OTP
        Returns:
            str: hashed otp
        """
        otp = random.randint(10**(max_lenght-1), 10**max_lenght - 1)

        hashed_otp = bcrypt.hashpw(
            str(otp).encode(),
            bcrypt.gensalt(10)
        ).decode()

        return otp, hashed_otp
    