from pydantic import BaseModel, EmailStr, ValidationError, conint, constr


class UserRegister(BaseModel):
    username: constr(min_length=5)
    email: EmailStr
    age: conint(ge=18)


def validate_user_registration(payload: dict) -> UserRegister:
    return UserRegister(**payload)


if __name__ == "__main__":
    valid_payload = {
        "username": "sarah99",
        "email": "sarah@example.com",
        "age": 24,
    }
    invalid_payload = {
        "username": "sam",
        "email": "not-an-email",
        "age": 16,
    }

    try:
        user = validate_user_registration(valid_payload)
        print("Valid input accepted:", user.model_dump())
    except ValidationError as exc:
        print("Valid payload unexpectedly failed:", exc)

    try:
        validate_user_registration(invalid_payload)
    except ValidationError as exc:
        print("Invalid input rejected:")
        print(exc)
