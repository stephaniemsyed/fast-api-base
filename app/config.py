from dynaconf import Dynaconf

settings = Dynaconf(
    settings_files=["app/settings.toml"],
    environments=True,
    load_dotenv=True,
    env_switcher="ENV",
)
