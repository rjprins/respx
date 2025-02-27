from typing import (
    Any,
    AsyncIterable,
    Awaitable,
    Callable,
    Dict,
    Iterable,
    Iterator,
    List,
    Optional,
    Pattern,
    Sequence,
    Tuple,
    Type,
    TypeVar,
    Union,
)

import httpx

URL = Tuple[
    bytes,  # scheme
    bytes,  # host
    Optional[int],  # port
    bytes,  # path
]
Headers = List[Tuple[bytes, bytes]]
Content = Union[str, bytes, Iterable[bytes], AsyncIterable[bytes]]

HeaderTypes = Union[
    httpx.Headers,
    Dict[str, str],
    Dict[bytes, bytes],
    Sequence[Tuple[str, str]],
    Sequence[Tuple[bytes, bytes]],
]
CookieTypes = Union[Dict[str, str], Sequence[Tuple[str, str]]]

DefaultType = TypeVar("DefaultType", bound=Any)

URLPatternTypes = Union[str, Pattern[str], URL, httpx.URL]
QueryParamTypes = Union[
    bytes, str, List[Tuple[str, Any]], Dict[str, Any], Tuple[Tuple[str, Any], ...]
]

ResolvedResponseTypes = Optional[Union[httpx.Request, httpx.Response]]
RouteResultTypes = Union[ResolvedResponseTypes, Awaitable[ResolvedResponseTypes]]
CallableSideEffect = Callable[..., RouteResultTypes]
SideEffectListTypes = Union[httpx.Response, Exception, Type[Exception]]
SideEffectTypes = Union[
    CallableSideEffect,
    Exception,
    Type[Exception],
    Iterator[SideEffectListTypes],
]
