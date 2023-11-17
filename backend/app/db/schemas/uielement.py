from decimal import Decimal
from enum import Enum
from typing import List, Optional  # noqa: F401, E261
# from datetime import datetime
from pydantic import UUID4, BaseModel, EmailStr
from enum import Enum
from typing import List
from enum import Enum


class UIElementBase(BaseModel):
    class UIElementTypeEnum(str, Enum):
        Label = 'Label'
        Input_Field = 'Input Field'
        Text_Area = 'Text Area'
        Checkbox = 'Checkbox'
        Radio_Button = 'Radio Button'
        Dropdown = 'Dropdown'
        Date_Picker = 'Date Picker'
        Time_Picker = 'Time Picker'
        File_Upload = 'File Upload'
        Image = 'Image'
        Icon = 'Icon'
        Link = 'Link'
        Tooltip = 'Tooltip'
        Slider = 'Slider'
    

    EntityID: Optional[int] = None
    ElementType: Optional[str] = None
    ElementName: Optional[str] = None
    ElementDescription: Optional[str] = None
    TypingMask: Optional[str] = None
    ValidationRules: Optional[str] = None
    SystemID: Optional[int] = None


class UIElementCreate(UIElementBase):
    class UIElementTypeEnum(str, Enum):
        Label = 'Label'
        Input_Field = 'Input Field'
        Text_Area = 'Text Area'
        Checkbox = 'Checkbox'
        Radio_Button = 'Radio Button'
        Dropdown = 'Dropdown'
        Date_Picker = 'Date Picker'
        Time_Picker = 'Time Picker'
        File_Upload = 'File Upload'
        Image = 'Image'
        Icon = 'Icon'
        Link = 'Link'
        Tooltip = 'Tooltip'
        Slider = 'Slider'
    
    EntityID: int
    ElementType: str
    ElementName: str
    ElementDescription: str
    TypingMask: str
    ValidationRules: str
    SystemID: int


class UIElementUpdate(UIElementBase):
    class UIElementTypeEnum(str, Enum):
        Label = 'Label'
        Input_Field = 'Input Field'
        Text_Area = 'Text Area'
        Checkbox = 'Checkbox'
        Radio_Button = 'Radio Button'
        Dropdown = 'Dropdown'
        Date_Picker = 'Date Picker'
        Time_Picker = 'Time Picker'
        File_Upload = 'File Upload'
        Image = 'Image'
        Icon = 'Icon'
        Link = 'Link'
        Tooltip = 'Tooltip'
        Slider = 'Slider'
        
    EntityID: Optional[int] = None
    ElementType: Optional[str] = None
    ElementName: Optional[str] = None
    ElementDescription: Optional[str] = None
    TypingMask: Optional[str] = None
    ValidationRules: Optional[str] = None
    SystemID: Optional[int] = None


class UIElementInDBBase(UIElementBase):
    id: int
    class Config:
        orm_mode = True


class UIElement(UIElementInDBBase):
    pass


class UIElementInDB(UIElementInDBBase):
    pass


