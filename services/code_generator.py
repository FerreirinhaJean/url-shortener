import random
import string


class CodeGenerator:
    def generate(self, length: int = 12) -> str:
        return "".join(
            random.choices(string.ascii_letters + string.digits, k=length)
        )
