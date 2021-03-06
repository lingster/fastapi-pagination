from typing import Optional, Sequence, TypeVar

from .api import create_page, resolve_params
from .bases import AbstractPage, AbstractParams

T = TypeVar("T")


def paginate(
    sequence: Sequence[T],
    params: Optional[AbstractParams] = None,
) -> AbstractPage[T]:
    params = resolve_params(params)
    raw_params = params.to_raw_params()

    return create_page(
        items=sequence[raw_params.offset : raw_params.offset + raw_params.limit],
        total=len(sequence),
        params=params,
    )


__all__ = ["paginate"]
