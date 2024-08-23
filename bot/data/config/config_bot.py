from data.config.secret_config import SecretConfig

config = SecretConfig()

async def load_bot_config() -> dict:
    """Load configuration settings from SecretConfig."""
    always_private = config.get_secret(key='If_ALWAYS_PRIVATE', default=0)
    interval = float(config.get_secret(key='ANTI_FLOOD_INTERVAL', default=0.5))
    always_private = bool(int(always_private))

    return {
        'always_private': always_private,
        'interval': interval
    }