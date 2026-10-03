

from model_utils.models import UUIDModel, TimeStampedModel, SoftDeletableModel

class BaseModel(UUIDModel, TimeStampedModel):
    """
    The purpose of this model is to wrap the common model_util bases into one
    abstract inheritable model to avoid having each of these inherited by every model.
    """

    class Meta:
        abstract = True

class SoftDeletableBaseModel(BaseModel, SoftDeletableModel):
    """
    The purpose of this model is to introduce a SoftDeletable variant of the
    above model.
    """

    class Meta:
        abstract = True
