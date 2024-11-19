from typing import Tuple, Type

from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
    PyprojectTomlConfigSettingsSource,
    PydanticBaseSettingsSource,
)


from models.base import ESConnectionMeta


class ProjectConfig(BaseSettings):

    name: str
    version: str = "0.1.0"
    description: str = ""
    authors: list[str] = []

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: Type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> Tuple[PydanticBaseSettingsSource, ...]:
        return (PyprojectTomlConfigSettingsSource(settings_cls),)

    model_config = SettingsConfigDict(
        pyproject_toml_table_header=("tool", "poetry"), extra="ignore"
    )

    @property
    def title(self) -> str:
        return self.name.replace("-", " ").title()


class ApplicationConfig(BaseSettings):

    # es_meta: ESConnectionMeta

    model_config = SettingsConfigDict(
        extra="ignore",
        env_nested_delimiter="__",
        env_file=".env",
        env_file_encoding="utf-8",
    )
