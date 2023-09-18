from dotenv import load_dotenv

import uvicorn


def main():
    load_dotenv()
    uvicorn.run(
        app="app.server:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        workers=1,
    )


if __name__ == "__main__":
    main()
