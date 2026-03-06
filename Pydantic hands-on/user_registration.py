from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class Address(BaseModel):
    city: str = Field(min_length=3)
    pincode: str = Field(min_length=6, max_length=6, regex=r'^\d{6}$')

    class Config:
        validate_assignment = True

class User(BaseModel):
    user_id: int
    name: str
    email: EmailStr
    age: int = Field(ge=18)
    address: Address
    is_premium: Optional[bool] = False

    class Config:
        validate_assignment = True

if __name__ == "__main__":
    try:
        # Create a valid user
        user = User(
            user_id=1,
            name="Alice",
            email="alice@example.com",
            age=25,
            address=Address(city="New York", pincode="100001")
        )
        print("Successfully created user:")
        print(user.json(indent=2))
        
        # Test assignment Validation
        print("\nTesting validation on assignment...")
        try:
            user.age = 17
            print("Failed to catch invalid age assignment.")
        except Exception as e:
            print("Validation caught error on age assignment as expected:", type(e).__name__)
            
        try:
            user.address.pincode = "123"
            print("Failed to catch invalid pincode assignment.")
        except Exception as e:
            print("Validation caught error on pincode assignment as expected:", type(e).__name__)
            
    except Exception as e:
        print("Unexpected Error:", e)
