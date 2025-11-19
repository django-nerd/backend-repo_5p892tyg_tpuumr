"""
Database Schemas for Unnamed (MVP)

Each Pydantic model maps to a MongoDB collection (lowercased class name).
"""
from pydantic import BaseModel, Field
from typing import Optional, List, Literal
from datetime import datetime

class Contact(BaseModel):
    label: str = Field(..., description="Human-friendly name")
    address: str = Field(..., description="Wallet address")
    notes: Optional[str] = None

class Ticket(BaseModel):
    email: str
    category: Literal["General","Account","Security","Payments","Bug"] = "General"
    message: str
    status: Literal["Open","In progress","Resolved"] = "Open"

class Setting(BaseModel):
    key: str
    value: dict

class Notification(BaseModel):
    kind: Literal["security","transaction","market"] = "security"
    title: str
    body: str
    created_at: Optional[datetime] = None
    read: bool = False

class Approval(BaseModel):
    token: str
    dapp: str
    amount: str
    unlimited: bool = False

class PortfolioSnapshot(BaseModel):
    currency: Literal["USD","EUR","SEK"] = "USD"
    total: float = 0.0
    updated_at: Optional[datetime] = None
