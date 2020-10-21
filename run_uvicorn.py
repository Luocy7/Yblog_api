import uvicorn
import os


def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")
    uvicorn.run(
        "config.asgi:application",
        host="127.0.0.1",
        port=8001,
        log_level="debug",
        reload=True,
    )


if __name__ == "__main__":
    main()
