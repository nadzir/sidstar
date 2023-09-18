from dotenv import load_dotenv
import os
import uvicorn


def main():
    load_dotenv()
    env = os.environ.get("ENV", False)
    uvicorn.run(
        app="app.server:app",
        host="0.0.0.0",
        port=8000,
        reload=True if env == "dev" else False,
        workers=1,
    )


if __name__ == "__main__":
    main()
