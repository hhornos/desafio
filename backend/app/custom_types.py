"""app.custom_types
Module that contains custom types
"""
from typing import (
    Dict,
    Sequence,
    Tuple,
    Union,
    Mapping,
    List,
    Optional,
)

StrOrBytes = Union[str, bytes]

PrimitiveData = Optional[Union[str, int, float, bool]]

HeaderTypes = Union[
    "Headers", Dict[StrOrBytes, StrOrBytes], Sequence[Tuple[StrOrBytes, StrOrBytes]],
]

QueryParamTypes = Union[
    "QueryParams",
    Mapping[str, Union[PrimitiveData, Sequence[PrimitiveData]]],
    List[Tuple[str, PrimitiveData]],
    str,
]
