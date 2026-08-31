

from model_utils.models import UUIDModel, TimeStampedModel, SoftDeletableModel

class BaseModel(UUIDModel, TimeStampedModel):

    class Meta:
        abstract = True

class SoftDeletableBaseModel(BaseModel, SoftDeletableModel):

    class Meta:
        abstract = True
