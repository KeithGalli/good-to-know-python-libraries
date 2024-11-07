from pydantic import BaseModel, Field

# from rich import console, traceback
# traceback.install()

class Account(BaseModel, validate_assignment=True):
    account_id: int = Field(..., frozen=True)
    name: str
    email: str
    password: str  # Make frozen

if __name__ == '__main__':
    account = Account(account_id=1, name='Jo', email="joe", password="123")

    print(account)
