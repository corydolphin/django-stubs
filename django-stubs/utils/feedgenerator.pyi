# Stubs for django.utils.feedgenerator (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

from io import StringIO
from datetime import date, datetime
from django.http.response import HttpResponse
from django.utils.safestring import SafeText
from django.utils.xmlutils import SimplerXMLGenerator
from typing import Any, Dict, List, Optional, Tuple, Union

def rfc2822_date(date: date) -> str: ...
def rfc3339_date(date: datetime) -> str: ...
def get_tag_uri(url: str, date: datetime) -> str: ...

class SyndicationFeed:
    feed: Any = ...
    items: Any = ...
    def __init__(
        self,
        title: str,
        link: str,
        description: str,
        language: Optional[str] = ...,
        author_email: Optional[str] = ...,
        author_name: Optional[str] = ...,
        author_link: Optional[str] = ...,
        subtitle: Optional[str] = ...,
        categories: Optional[Tuple[str, str]] = ...,
        feed_url: Optional[str] = ...,
        feed_copyright: Optional[str] = ...,
        feed_guid: Optional[str] = ...,
        ttl: Optional[int] = ...,
        **kwargs: Any,
    ) -> None: ...
    def add_item(
        self,
        title: SafeText,
        link: str,
        description: str,
        author_email: Optional[str] = ...,
        author_name: Optional[str] = ...,
        author_link: Optional[str] = ...,
        pubdate: Optional[datetime] = ...,
        comments: None = ...,
        unique_id: str = ...,
        unique_id_is_permalink: Optional[bool] = ...,
        categories: Optional[Tuple[str, str]] = ...,
        item_copyright: Optional[str] = ...,
        ttl: None = ...,
        updateddate: Optional[datetime] = ...,
        enclosures: List[Enclosure] = ...,
        **kwargs: Any,
    ) -> None: ...
    def num_items(self): ...
    def root_attributes(self) -> Dict[Any, Any]: ...
    def add_root_elements(self, handler: Any) -> None: ...
    def item_attributes(self, item: Dict[str, Any]) -> Dict[Any, Any]: ...
    def add_item_elements(self, handler: Any, item: Any) -> None: ...
    def write(self, outfile: Any, encoding: Any) -> None: ...
    def writeString(self, encoding: str) -> str: ...
    def latest_post_date(self) -> datetime: ...

class Enclosure:
    url: Any = ...
    def __init__(self, url: str, length: Union[str, int], mime_type: str) -> None: ...

class RssFeed(SyndicationFeed):
    content_type: str = ...
    def write(self, outfile: HttpResponse, encoding: str) -> None: ...
    def rss_attributes(self) -> Dict[str, str]: ...
    def write_items(self, handler: SimplerXMLGenerator) -> None: ...
    def add_root_elements(self, handler: SimplerXMLGenerator) -> None: ...
    def endChannelElement(self, handler: SimplerXMLGenerator) -> None: ...

class RssUserland091Feed(RssFeed):
    _version: str = ...
    def add_item_elements(
        self, handler: SimplerXMLGenerator, item: Dict[str, Any]
    ) -> None: ...

class Rss201rev2Feed(RssFeed):
    _version: str = ...
    def add_item_elements(
        self, handler: SimplerXMLGenerator, item: Dict[str, Any]
    ) -> None: ...

class Atom1Feed(SyndicationFeed):
    content_type: str = ...
    ns: str = ...
    def write(self, outfile: Union[StringIO, HttpResponse], encoding: str) -> None: ...
    def root_attributes(self) -> Dict[str, str]: ...
    def add_root_elements(self, handler: SimplerXMLGenerator) -> None: ...
    def write_items(self, handler: SimplerXMLGenerator) -> None: ...
    def add_item_elements(
        self, handler: SimplerXMLGenerator, item: Dict[str, Any]
    ) -> None: ...

DefaultFeed = Rss201rev2Feed