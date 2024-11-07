from pydantic import BaseModel, SecretStr, Field, field_validator

class Account(BaseModel, validate_assignment=True):
    account_id: int
    username: str = Field(..., min_length=4, max_length=16, )
    password: SecretStr

    @field_validator('account_id')
    def check_account_id(cls, v):
        if v < 0:
            raise ValueError('Account ID must be greater than 0')
        return v

if __name__ == '__main__':
    account = Account(account_id=-5, username="kdawg", password='hello123')
    print(account)

