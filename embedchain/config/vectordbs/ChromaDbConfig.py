from typing import Optional

from embedchain.config.vectordbs.BaseVectorDbConfig import BaseVectorDbConfig
from embedchain.helper.json_serializable import register_deserializable


@register_deserializable
class ChromaDbConfig(BaseVectorDbConfig):
    def __init__(
        self,
        collection_name: Optional[str] = None,
        dir: Optional[str] = None,
        host: Optional[str] = None,
        port: Optional[str] = None,
        chroma_settings: Optional[dict] = None,
    ):
        """
        Initializes a configuration class instance for ChromaDB.

        :param collection_name: Default name for the collection, defaults to None
        :type collection_name: Optional[str], optional
        :param dir: Path to the database directory, where the database is stored, defaults to None
        :type dir: Optional[str], optional
        :param host: Database connection remote host. Use this if you run Embedchain as a client, defaults to None
        :type host: Optional[str], optional
        :param port: Database connection remote port. Use this if you run Embedchain as a client, defaults to None
        :type port: Optional[str], optional
        :param chroma_settings: Chroma settings dict, defaults to None
        :type chroma_settings: Optional[dict], optional
        """
        """
        :param chroma_settings: Optional. Chroma settings for connection.
        """
        self.chroma_settings = chroma_settings
        super().__init__(collection_name=collection_name, dir=dir, host=host, port=port)
