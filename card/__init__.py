from pydantic import BaseModel, Field


class RegisterCardModel(BaseModel):
    card_number: int
    card_name: str
    exp_date: int = Field(lt=1299, gt=123)
    cvv: int = Field(lt=1000, ge=0)
    bank: str
    balance: float = Field(ge=0)

