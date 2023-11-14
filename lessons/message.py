"""Class to store a message (operator overload, union types, default parameters)."""

class Email:

    to: str | int
    message: str
    important: bool

    def __init__(self, recipient: str | int, messsage_text: str = "", importance_flag: bool = False): # put default variables at the end
        """Constructor of an email."""
        self.to = recipient
        self.message = messsage_text
        self.important = importance_flag

    def __str__(self) -> str:
        m_string: str = f"To: {self.to}\n"
        m_string += f"Important? {self.important}\n"
        m_string += f'"{self.message}"'
        return m_string
    
    def __mul__(self, factor: int):
        self.message *= factor

email_to_chiara: Email = Email("Chiara", "You're a great TA!", False)
email_to_chiara * 5
print(email_to_chiara)

email_to_lauren: Email = Email("Lauren", "Great job!")
print(email_to_lauren)

email_to_samantha: Email = Email(730642818, "Hooray!", True)
print(email_to_samantha)