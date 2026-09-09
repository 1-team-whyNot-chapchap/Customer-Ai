"""Local single-process entry point matching Customer-Service's AI endpoint."""

import uvicorn


def main() -> None:
    uvicorn.run(
        "chapchap_customer_ai.main:create_app",
        factory=True,
        host="127.0.0.1",
        port=8085,
        workers=1,
    )


if __name__ == "__main__":
    main()
